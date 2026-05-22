#!/usr/bin/env python3
"""
Flask Web Application for Meter Detection
Provides REST API endpoints for image upload and detection
"""

import os
import sys
import sqlite3
from pathlib import Path
from datetime import datetime
from werkzeug.utils import secure_filename

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    session,
    send_file,
    flash,
)
from flask_cors import CORS
import torch
import cv2
import numpy as np
from PIL import Image
import io
import base64
import logging
import pandas as pd  # for Excel export [web:10]

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Configuration
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "bmp"}
MAX_FILE_SIZE = 1024 * 1024 * 1024  # 1024MB
BASE_DIR = Path(__file__).parent.parent
UPLOAD_FOLDER = BASE_DIR / "uploads"
MODELS_FOLDER = BASE_DIR / "models" / "meter_detection" / "weights"
DB_PATH = BASE_DIR / "detections.db"

# Create uploads folder
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

# ------------------ NEW: VIDEO FOLDER ------------------
VIDEO_UPLOAD_FOLDER = BASE_DIR / "uploaded_videos"
VIDEO_UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

# ------------------ NEW: RUNTIME HISTORY (PER USER) ------------------
# { "email@example.com": [ { "timestamp": ..., "filename": ..., "has_meter": ..., "meters_count": ..., "non_meters_count": ... }, ... ] }
RUNTIME_HISTORY = {}

# ------------------ NEW: SIMPLE VIRTUAL USER DB ------------------
# { "email@example.com": {"password": "1234"} }
USERS_DB = {}


def init_db():
    """Initialize SQLite database for detection logs"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS detection_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            filename TEXT NOT NULL,
            has_meter INTEGER NOT NULL,
            meters_count INTEGER NOT NULL,
            non_meters_count INTEGER NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """
    
    )
    conn.commit()
    conn.close()


class MeterDetector:
    """Meter detection using YOLOv5 model"""

    def __init__(self, model_path=None):
        """Initialize detector with trained model"""
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Using device: {self.device}")

        # Load YOLOv5 model
        if model_path is None:
            model_path = MODELS_FOLDER / "best.pt"

        if not Path(model_path).exists():
            logger.warning(f"Model not found at {model_path}")
            self.model = None
        else:
            try:
                self.model = torch.hub.load(
                    "ultralytics/yolov5",
                    "custom",
                    path=str(model_path),
                    force_reload=False,
                )
                self.model.to(self.device)
                self.model.eval()
                logger.info(f"Model loaded successfully from {model_path}")
            except Exception as e:
                logger.error(f"Failed to load model: {e}")
                self.model = None

    def detect(self, image_path, conf_threshold=0.20):
        """
        Detect meters in image

        Args:
            image_path: Path to image file
            conf_threshold: Confidence threshold (0.20 = 20%)

        Returns:
            dict: Detection results with confidence scores
        """
        if self.model is None:
            return {
                "success": False,
                "error": "Model not loaded",
                "detections": [],
            }

        try:
            # Read and validate image
            image = Image.open(image_path).convert("RGB")

            # Run inference
            results = self.model(image, size=640)

            # Extract detections
            detections = []
            predictions = results.xyxy[0].cpu().numpy()

            for pred in predictions:
                x1, y1, x2, y2, conf, cls = pred
                confidence = float(conf) * 100  # Convert to percentage

                detection = {
                    "bbox": {
                        "x1": float(x1),
                        "y1": float(y1),
                        "x2": float(x2),
                        "y2": float(y2),
                    },
                    "confidence": confidence,
                    "is_meter": confidence >= conf_threshold * 100,
                    "class": int(cls),
                }
                detections.append(detection)

            # Generate annotated image
            annotated_image = self._draw_detections(image, predictions, conf_threshold)

            return {
                "success": True,
                "detections": detections,
                "annotation_count": len(detections),
                "annotated_image": annotated_image,
                "has_meter": any(d["is_meter"] for d in detections),
            }

        except Exception as e:
            logger.error(f"Detection error: {e}")
            return {
                "success": False,
                "error": str(e),
                "detections": [],
            }

    def _draw_detections(self, image, predictions, conf_threshold):
        """Draw bounding boxes on image"""
        try:
            img_np = np.array(image)
            threshold_pct = conf_threshold * 100

            for pred in predictions:
                x1, y1, x2, y2, conf, cls = pred
                confidence = float(conf) * 100

                # Color based on threshold
                if confidence >= threshold_pct:
                    color = (0, 255, 0)  # Green for meter
                    label = f"METER {confidence:.1f}%"
                else:
                    color = (255, 0, 0)  # Red for non-meter
                    label = f"NOT METER {confidence:.1f}%"

                # Draw box
                cv2.rectangle(
                    img_np,
                    (int(x1), int(y1)),
                    (int(x2), int(y2)),
                    color,
                    2,
                )

                # Draw label
                (text_width, text_height), _ = cv2.getTextSize(
                    label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2
                )
                cv2.rectangle(
                    img_np,
                    (int(x1), int(y1) - text_height - 10),
                    (int(x1) + text_width, int(y1)),
                    color,
                    -1,
                )
                cv2.putText(
                    img_np,
                    label,
                    (int(x1), int(y1) - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    1,
                )

            return Image.fromarray(img_np)
        except Exception as e:
            logger.error(f"Drawing error: {e}")
            return image


def allowed_file(filename):
    """Check if file extension is allowed"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ------------------ AUTH HELPERS ------------------
def current_user_email():
    return session.get("user_email")


def require_login():
    return current_user_email() is not None


def create_app():
    """Create and configure Flask application"""
    app = Flask(__name__)
    # keep your previous config and extend
    app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE
    app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)
    app.config["VIDEO_UPLOAD_FOLDER"] = str(VIDEO_UPLOAD_FOLDER)
    app.secret_key = "change_this_to_a_random_secret_key"

    # init database
    init_db()

    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Initialize detector
    detector = MeterDetector()

    # --------------- AUTH ROUTES ---------------
    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "POST":
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "").strip()

            if not email or not password:
                flash("Email and password are required.")
                return redirect(url_for("signup"))

            # Check if user already exists in SQLite
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT id FROM users WHERE email = ?", (email,))
            row = cur.fetchone()

            if row:
                conn.close()
                flash("User already exists. Please login.")
                return redirect(url_for("login"))

            # Insert new user in SQLite
            cur.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                (email, password),
            )
            conn.commit()
            conn.close()

            # Optional: initialize runtime history dict entry (keeps your existing behavior)
            if email not in RUNTIME_HISTORY:
                RUNTIME_HISTORY[email] = []

            flash("Signup successful. Please login.")
            return redirect(url_for("login"))

        return render_template("login.html", mode="signup")


    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "").strip()
    
            # Read user from SQLite instead of USERS_DB
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute(
                "SELECT id, password FROM users WHERE email = ?",
                (email,),
            )
            row = cur.fetchone()
            conn.close()
    
            # if no user or password mismatch -> invalid
            if not row or row[1] != password:
                flash("Invalid email or password.")
                return redirect(url_for("login"))
    
            # valid login: create session
            session["user_email"] = email
    
            # optional: keep your runtime history init
            if email not in RUNTIME_HISTORY:
                RUNTIME_HISTORY[email] = []
    
            return redirect(url_for("index"))
    
        return render_template("login.html", mode="login")


    @app.route("/logout")
    def logout():
        session.pop("user_email", None)
        return redirect(url_for("login"))

    # --------------- FRONTEND MAIN PAGE ---------------
    @app.route("/", methods=["GET"])
    def index():
        # Require login for frontend
        if not require_login():
            return redirect(url_for("login"))

        return render_template("index.html", user_email=current_user_email())

    # --------------- HEALTH ENDPOINT (unchanged) ---------------
    @app.route("/api/health", methods=["GET"])
    def health():
        """Health check endpoint"""
        return (
            jsonify(
                {
                    "status": "OK",
                    "timestamp": datetime.now().isoformat(),
                    "model_loaded": detector.model is not None,
                    "device": str(detector.device),
                }
            ),
            200,
        )

    # --------------- DETECT ENDPOINT (unchanged logic, plus runtime history) ---------------
    @app.route("/api/detect", methods=["POST"])
    def detect():
        """
        Upload and detect meters in images

        Form data:
            - images: Multiple image files

        Returns:
            JSON with detection results
        """
        try:
            # Check for files
            if "images" not in request.files:
                return jsonify({
                    "success": False,
                    "error": "No images provided",
                }), 400

            files = request.files.getlist("images")

            # Fixed confidence threshold: 0.20 (20%)
            conf_threshold = 0.20
            logger.info(f"Using confidence threshold (fixed): {conf_threshold}")

            if not files or len(files) == 0:
                return jsonify({
                    "success": False,
                    "error": "No images provided",
                }), 400

            results = {
                "success": True,
                "timestamp": datetime.now().isoformat(),
                "total_images": len(files),
                "results": [],
                "summary": {
                    "total_detections": 0,
                    "meters_detected": 0,
                    "non_meters": 0,
                },
            }

            # logged-in user
            user_email = current_user_email()

            for file in files:
                if not allowed_file(file.filename):
                    results["results"].append({
                        "filename": file.filename,
                        "success": False,
                        "error": "File type not allowed",
                    })
                    continue

                try:
                    # Save uploaded file
                    filename = secure_filename(file.filename)
                    ts = datetime.now().strftime("%Y%m%d_%H%M%S_")
                    saved_filename = ts + filename
                    filepath = UPLOAD_FOLDER / saved_filename

                    file.save(str(filepath))
                    logger.info(f"Saved upload: {saved_filename}")

                    # Run detection
                    detection_result = detector.detect(str(filepath), conf_threshold)

                    # Convert annotated image to base64
                    annotated_b64 = None
                    if detection_result["success"] and detection_result.get("annotated_image"):
                        img_buffer = io.BytesIO()
                        detection_result["annotated_image"].save(img_buffer, format="JPEG")
                        img_buffer.seek(0)
                        annotated_b64 = base64.b64encode(img_buffer.getvalue()).decode()

                    result_entry = {
                        "filename": filename,
                        "success": detection_result["success"],
                        "detections": detection_result.get("detections", []),
                        "annotation_count": detection_result.get("annotation_count", 0),
                        "has_meter": detection_result.get("has_meter", False),
                        "annotated_image": annotated_b64,
                    }

                    if not detection_result["success"]:
                        result_entry["error"] = detection_result.get("error")

                    results["results"].append(result_entry)

                    # Update summary and log to DB + runtime history
                    if detection_result["success"]:
                        meters_count = sum(
                            1 for d in detection_result.get("detections", [])
                            if d["is_meter"]
                        )
                        non_meters_count = sum(
                            1 for d in detection_result.get("detections", [])
                            if not d["is_meter"]
                        )

                        results["summary"]["total_detections"] += len(
                            detection_result.get("detections", [])
                        )
                        results["summary"]["meters_detected"] += meters_count
                        results["summary"]["non_meters"] += non_meters_count

                        # Log to SQLite (existing)
                        try:
                            conn = sqlite3.connect(DB_PATH)
                            cur = conn.cursor()
                            cur.execute(
                                """
                                INSERT INTO detection_log (
                                    timestamp, filename, has_meter, meters_count, non_meters_count
                                )
                                VALUES (?, ?, ?, ?, ?)
                                """,
                                (
                                    datetime.now().isoformat(),
                                    filename,
                                    1 if detection_result.get("has_meter", False) else 0,
                                    meters_count,
                                    non_meters_count,
                                ),
                            )
                            conn.commit()
                            conn.close()
                        except Exception as db_err:
                            logger.error(f"Failed to log detection to DB: {db_err}")

                        # Add runtime history for Excel
                        if user_email:
                            if user_email not in RUNTIME_HISTORY:
                                RUNTIME_HISTORY[user_email] = []
                            RUNTIME_HISTORY[user_email].append(
                                {
                                    "timestamp": datetime.now().isoformat(),
                                    "filename": filename,
                                    "has_meter": bool(detection_result.get("has_meter", False)),
                                    "meters_count": meters_count,
                                    "non_meters_count": non_meters_count,
                                }
                            )

                    logger.info(f"Detection complete: {filename}")

                except Exception as e:
                    logger.error(f"Error processing {file.filename}: {e}")
                    results["results"].append({
                        "filename": file.filename,
                        "success": False,
                        "error": str(e),
                    })

            return jsonify(results), 200

        except Exception as e:
            logger.error(f"Upload error: {e}")
            return jsonify({
                "success": False,
                "error": str(e),
            }), 500



    # --------------- CONFIG ENDPOINT (unchanged) ---------------
    @app.route("/api/config", methods=["GET"])
    def config():
        """Get application configuration"""
        return (
            jsonify(
                {
                    "allowed_extensions": list(ALLOWED_EXTENSIONS),
                    "max_file_size_mb": MAX_FILE_SIZE / (1024 * 1024),
                    "conf_threshold_default": 0.20,
                    "model_info": {
                        "name": "YOLOv5s Meter Detection",
                        "framework": "PyTorch",
                        "device": str(detector.device),
                    },
                }
            ),
            200,
        )

    # --------------- STATS ENDPOINTS (unchanged) ---------------
    @app.route("/api/stats", methods=["GET"])
    def stats():
        """Return detection statistics from database"""
        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()

            cur.execute("SELECT COUNT(*) FROM detection_log")
            total_rows = cur.fetchone()[0]

            cur.execute(
                "SELECT SUM(meters_count), SUM(non_meters_count) FROM detection_log"
            )
            row = cur.fetchone()
            total_meters = row[0] or 0
            total_non_meters = row[1] or 0

            cur.execute(
                """
                SELECT timestamp, filename, has_meter, meters_count, non_meters_count
                FROM detection_log
                ORDER BY id DESC
                LIMIT 50
            """
            )
            rows = cur.fetchall()
            conn.close()

            history = [
                {
                    "timestamp": r[0],
                    "filename": r[1],
                    "has_meter": bool(r[2]),
                    "meters_count": r[3],
                    "non_meters_count": r[4],
                }
                for r in rows
            ]

            return (
                jsonify(
                    {
                        "success": True,
                        "total_rows": total_rows,
                        "total_meters": total_meters,
                        "total_non_meters": total_non_meters,
                        "history": history,
                    }
                ),
                200,
            )

        except Exception as e:
            logger.error(f"Stats error: {e}")
            return (
                jsonify(
                    {
                        "success": False,
                        "error": str(e),
                    }
                ),
                500,
            )

    @app.route("/api/stats/reset", methods=["POST"])
    def reset_stats():
        """Delete all detection history"""
        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("DELETE FROM detection_log")
            conn.commit()
            conn.close()
            return (
                jsonify(
                    {
                        "success": True,
                        "message": "Detection history cleared",
                    }
                ),
                200,
            )
        except Exception as e:
            logger.error(f"Reset stats error: {e}")
            return (
                jsonify(
                    {
                        "success": False,
                        "error": str(e),
                    }
                ),
                500,
            )

    # --------------- NEW: VIDEO UPLOAD ROUTE ---------------
    @app.route("/upload_video", methods=["POST"])
    def upload_video():
        if not require_login():
            return redirect(url_for("login"))

        if "video_file" not in request.files:
            flash("No video file part found.")
            return redirect(url_for("index"))

        video = request.files["video_file"]
        if video.filename == "":
            flash("No video selected.")
            return redirect(url_for("index"))

        video_filename = secure_filename(video.filename)
        video_path = VIDEO_UPLOAD_FOLDER / video_filename
        video.save(str(video_path))
        flash("Video uploaded successfully.")
        return redirect(url_for("index"))

    # --------------- NEW: HISTORY DOWNLOAD (EXCEL) ---------------
    @app.route("/download_history")
    def download_history():
        if not require_login():
            return redirect(url_for("login"))

        # 1) Read data from SQLite detection_log table
        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute(
                """
                SELECT timestamp, filename, has_meter, meters_count, non_meters_count
                FROM detection_log
                ORDER BY id DESC
                """
            )
            rows = cur.fetchall()
            conn.close()
        except Exception as e:
            logger.error(f"Download history DB error: {e}")
            rows = []

        # 2) Convert rows to list of dicts
        data = [
            {
                "timestamp": r[0],
                "filename": r[1],
                "has_meter": bool(r[2]),
                "meters_count": r[3],
                "non_meters_count": r[4],
            }
            for r in rows
        ]

        # 3) Build DataFrame from this data
        df = pd.DataFrame(
            data,
            columns=[
                "timestamp",
                "filename",
                "has_meter",
                "meters_count",
                "non_meters_count",
            ],
        )

        # 4) Write to Excel in memory
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:  # or openpyxl
            df.to_excel(writer, index=False, sheet_name="History")
        output.seek(0)

        # 5) Send file to user
        email = current_user_email() or "user"
        filename = f"meter_history_{email}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        return send_file(
            output,
            as_attachment=True,
            download_name=filename,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )


    # --------------- ERROR HANDLERS (unchanged) ---------------
    @app.errorhandler(413)
    def too_large(e):
        """Handle file too large error"""
        return (
            jsonify(
                {
                    "success": False,
                    "error": f"File too large. Maximum size: {MAX_FILE_SIZE / (1024*1024)}MB",
                }
            ),
            413,
        )

    @app.errorhandler(404)
    def not_found(e):
        """Handle 404 errors"""
        return (
            jsonify(
                {
                    "success": False,
                    "error": "Endpoint not found",
                }
            ),
            404,
        )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=False)
