from flask import Blueprint, render_template, request, jsonify, send_file
import os
import uuid
from werkzeug.utils import secure_filename
from app.config import Config
from app.detector import MeterDetector
from app.database import Database
import cv2
import base64
from io import BytesIO

bp = Blueprint('main', __name__)

# Initialize detector with YOUR trained model
detector = MeterDetector(Config.MODEL_PATH) if os.path.exists(Config.MODEL_PATH) else None

# Initialize database
db = Database()

def allowed_file(filename):
    """Check if file extension is allowed"""
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1).lower()
    return ext in Config.ALLOWED_EXTENSIONS

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    
    if 'files' not in request.files:
        return jsonify({'error': 'No files provided'}), 400
    
    files = request.files.getlist('files')
    
    # Generate unique upload ID
    upload_id = str(uuid.uuid4())
    
    # Create upload record
    db.create_upload(upload_id, len(files))
    
    results = {'good': [], 'bad': [], 'total': 0, 'upload_id': upload_id}
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            # Save input
            input_path = os.path.join(Config.UPLOAD_FOLDER, filename)
            os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
            file.save(input_path)
            
            # Detect using YOUR trained model
            if detector:
                result = detector.detect(input_path)
                accuracy = result['accuracy']
                
                # Determine if good or bad
                is_good = 1 if accuracy >= Config.GOOD_ACCURACY_THRESHOLD else 0
                
                # Save detection to database
                db.add_detection(upload_id, filename, float(accuracy), is_good)
                
                # Save annotated image
                if result['image_annotated'] is not None:
                    if is_good:
                        folder = Config.GOOD_FOLDER
                        results['good'].append(filename)
                    else:
                        folder = Config.BAD_FOLDER
                        results['bad'].append(filename)
                    
                    os.makedirs(folder, exist_ok=True)
                    output_path = os.path.join(folder, filename)
                    cv2.imwrite(output_path, result['image_annotated'])
                
                results['total'] += 1
    
    # Update upload statistics
    db.update_upload_stats(upload_id, len(results['good']), len(results['bad']))
    
    return jsonify(results)

@bp.route('/results')
def results():
    good_files = os.listdir(Config.GOOD_FOLDER) if os.path.exists(Config.GOOD_FOLDER) else []
    bad_files = os.listdir(Config.BAD_FOLDER) if os.path.exists(Config.BAD_FOLDER) else []
    
    return render_template('results.html', 
                         good_files=good_files, 
                         bad_files=bad_files)

@bp.route('/dashboard')
def dashboard():
    good_count = len(os.listdir(Config.GOOD_FOLDER)) if os.path.exists(Config.GOOD_FOLDER) else 0
    bad_count = len(os.listdir(Config.BAD_FOLDER)) if os.path.exists(Config.BAD_FOLDER) else 0
    total = good_count + bad_count
    
    stats = {
        'good': good_count,
        'bad': bad_count,
        'total': total,
        'accuracy': (good_count / total * 100) if total > 0 else 0
    }
    
    return render_template('dashboard.html', stats=stats)

@bp.route('/history')
def history():
    """View upload history and statistics"""
    upload_history = db.get_upload_history()
    overall_stats = db.get_statistics()
    
    return render_template('history.html', 
                         uploads=upload_history,
                         stats=overall_stats)

@bp.route('/upload-details/<upload_id>')
def upload_details(upload_id):
    """View details of a specific upload"""
    detections = db.get_upload_details(upload_id)
    
    return render_template('upload_details.html', 
                         upload_id=upload_id,
                         detections=detections)

@bp.route('/image/<type>/<filename>')
def get_image(type, filename):
    if type == 'good':
        path = os.path.join(Config.GOOD_FOLDER, filename)
    else:
        path = os.path.join(Config.BAD_FOLDER, filename)
    
    if os.path.exists(path):
        return send_file(path, mimetype='image/jpeg')
    return jsonify({'error': 'Not found'}), 404
