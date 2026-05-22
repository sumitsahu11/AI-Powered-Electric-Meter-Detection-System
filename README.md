<div align="center">
<img src="screenshots/slide_01.jpg" alt="Electric Meter Detection System" width="100%" />
<br/><br/>
 
# ⚡ Electric Meter Detection System
 
### Automated AI-Powered Electric Meter Detection using YOLOv5 Deep Learning
 
<br/>
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0.1-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![YOLOv5](https://img.shields.io/badge/YOLOv5-v7.0.13-00FFFF?style=for-the-badge&logo=github&logoColor=black)](https://github.com/ultralytics/yolov5)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8.1-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge)](.)
 
<br/>
> **Internship Project — TPCODL (TP Central Odisha Distribution Ltd.)**  
> Developed by **Sumit Kumar Sahu** · B.Tech CS (AI & ML) · 2026
 
<br/>
| 🎯 Precision | 📡 Recall | 📊 mAP@50 | ⚡ Speed | 📦 Model Size | 💰 Cost Saved | 🕐 Time Saved |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **95%+** | **96%** | **0.94** | **152 FPS** | **14 MB** | **90%** | **20×** |
 
</div>
---
 
## 📋 Table of Contents
 
- [📌 Executive Summary](#-executive-summary)
- [❗ Problem Statement](#-problem-statement)
- [✅ Proposed Solution](#-proposed-solution)
- [🛠️ Technology Stack](#%EF%B8%8F-technology-stack)
- [🏗️ System Architecture](#%EF%B8%8F-system-architecture)
- [🔬 Pipeline — All 5 Steps](#-pipeline--all-5-steps)
  - [Step 1 — Frame Extraction](#step-1--frame-extraction)
  - [Step 2 — Data Annotation](#step-2--data-annotation)
  - [Step 3 — Dataset Preparation](#step-3--dataset-preparation)
  - [Step 4 — Model Training](#step-4--model-training)
  - [Step 5 — Inference & Results](#step-5--inference--results)
- [🧠 Transfer Learning](#-transfer-learning--the-key-technique)
- [📁 Project File Structure](#-project-file-structure)
- [🌐 Flask REST API](#-flask-rest-api)
- [🖥️ Live Web Interface](#%EF%B8%8F-live-web-interface)
- [📈 Before vs After — Impact](#-before-vs-after--impact-analysis)
- [🏆 Conclusion](#-conclusion)
- [🔮 Future Scope](#-future-scope)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Configuration](#%EF%B8%8F-configuration)
- [🛠️ Troubleshooting](#%EF%B8%8F-troubleshooting)
- [👤 Author](#-author)
---
 
## 📌 Executive Summary
 
<img src="screenshots/slide_03.jpg" alt="Executive Summary" width="100%" />
<br/>
An **end-to-end automated electric meter detection system** powered by **YOLOv5 deep learning** to identify and precisely locate electric meters in images and videos. Built during an internship at **TPCODL**, this system replaces expensive, error-prone manual field inspections with a fully automated, scalable AI pipeline.
 
**Project Objectives:**
- 🎯 Automate detection of electric meters in field survey video footage
- ⏱️ Reduce inspection time from **40+ hours → under 2 hours** per building zone
- 🌐 Deploy as a **REST API** for seamless TPCODL infrastructure integration
- ✅ Achieve minimum 90% detection accuracy — **final result: 95%+ precision**
---
 
## ❗ Problem Statement
 
<img src="screenshots/slide_04.jpg" alt="Problem Statement" width="100%" />
<br/>
Manual electric meter inspection at TPCODL was **inefficient, expensive, and error-prone**:
 
| Issue | Old Way | Impact |
|-------|---------|--------|
| ⏱️ **Time Inefficiency** | 40+ hours/building | Field teams walk every floor, record manually |
| 💸 **High Cost** | ₹20,000–₹25,000/inspection | Unsustainable across hundreds of buildings |
| 👁️ **Human Error** | 5–10% meters missed | Revenue loss + compliance failures |
| 📋 **No Scalability** | 1 team, serial process | Cannot scale to TPCODL's growing grid |
 
---
 
## ✅ Proposed Solution
 
<img src="screenshots/slide_05.jpg" alt="Proposed Solution" width="100%" />
<br/>
A **5-step AI pipeline** that transforms raw survey videos into structured detection reports — automatically:
 
```
🎥 Video Input → 🖼️ Frame Extraction → 🏷️ Annotation → 🧠 Training → 🔍 Inference → 📊 Results
```
 
| Step | What Happens | Tool Used | Time |
|------|-------------|-----------|------|
| **1** | Extract frames from video | OpenCV | ~5 min |
| **2** | Manually annotate meters | LabelImg / Roboflow | ~60 min |
| **3** | Prepare train/val/test splits | Python | ~2 min |
| **4** | Train YOLOv5 model | YOLOv5 + PyTorch | ~120 min |
| **5** | Run inference + save results | PyTorch | ~5 min |
 
---
 
## 🛠️ Technology Stack
 
<img src="screenshots/slide_06.jpg" alt="Technology Stack" width="100%" />
<br/>
| Technology | Version | Role |
|-----------|---------|------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | `3.10+` | Core language |
| ![YOLOv5](https://img.shields.io/badge/-YOLOv5-00FFFF?logo=github&logoColor=black) | `v7.0.13` | Object detection (152 FPS, 14 MB model) |
| ![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?logo=pytorch&logoColor=white) | `2.0.1` | Deep learning + GPU acceleration |
| ![OpenCV](https://img.shields.io/badge/-OpenCV-5C3EE8?logo=opencv&logoColor=white) | `4.8.1` | Frame extraction + image manipulation |
| ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) | `2.3.3` | Lightweight REST API server |
| ![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white) | `1.24.3` | Numerical computing + matrix ops |
| ![Pillow](https://img.shields.io/badge/-Pillow-brightgreen) | `10.0.1` | Image load / save / transform |
| ![TorchVision](https://img.shields.io/badge/-TorchVision-EE4C2C?logo=pytorch&logoColor=white) | `0.15.2` | Vision transforms + dataset loaders |
| ![Flask-CORS](https://img.shields.io/badge/-Flask--CORS-000000?logo=flask&logoColor=white) | `4.0.0` | Cross-origin API access for browser clients |
 
---
 
## 🏗️ System Architecture
 
<img src="screenshots/slide_07.jpg" alt="System Architecture — 5-Step Pipeline" width="100%" />
<br/>
```
meter_detection_project/
│
├── 🎥  [VIDEO INPUT]         data/videos/
│           │
│           ▼
├── 🖼️  [STEP 1]  Frame Extraction  (OpenCV)     → data/frames/extracted/      (~5 min)
│           │
│           ▼
├── 🏷️  [STEP 2]  Manual Annotation (LabelImg)   → data/frames/annotated/      (~60 min)
│           │
│           ▼
├── 📂  [STEP 3]  Dataset Preparation (Python)   → data/dataset/  70/15/15     (~2 min)
│           │
│           ▼
├── 🧠  [STEP 4]  YOLOv5 Training (PyTorch)      → models/meter_detection/best.pt  (~120 min)
│           │
│           ▼
└── 📊  [STEP 5]  Inference & Results             → results/detections/ + SQLite + REST API
```
 
**Output:** Detection images with bounding boxes · Confidence scores · Precision / Recall / mAP · SQLite database · REST API JSON responses
 
---
 
## 🔬 Pipeline — All 5 Steps
 
---
 
### Step 1 — Frame Extraction
 
<img src="screenshots/slide_08.jpg" alt="Step 1 — Frame Extraction" width="100%" />
<br/>
```python
# Extracts every 5th frame from survey video using OpenCV
pipeline = MeterDetectionPipeline()
num_frames = pipeline.step1_extract_frames()
# Output: ~360 JPG images → data/frames/extracted/
```
 
**config.json settings:**
```json
"extraction": {
  "frame_interval": 5,    // every 5th frame
  "format": "jpg"
}
```
 
> **Why every 5th frame?** A 60-sec video at 30 FPS = 1,800 frames. Extracting every 5th gives ~360 images — sufficient temporal coverage while saving **80% disk space and processing time**.
 
**Visual Flow:**
```
INPUT                  OPENCV                   FILTER                  OUTPUT
sample_meter.mp4  →  cv2.VideoCapture()  →  frame_count % 5 == 0  →  frame_0001.jpg … frame_0360.jpg
data/videos/          Reads frame-by-frame       Keep every 5th            data/frames/extracted/
```
 
---
 
### Step 2 — Data Annotation
 
<img src="screenshots/slide_09.jpg" alt="Step 2 — Data Annotation" width="100%" />
<br/>
Annotation = teaching the AI: **"THIS is a meter"** — by drawing a bounding box around it in every image.
 
**Annotation Tools:**
 
| Tool | Type | Notes |
|------|------|-------|
| 🖥️ **LabelImg** | Desktop, open-source | Primary tool. Draws boxes, saves `.txt` in YOLO format |
| ☁️ **Roboflow** | Cloud-based | Upload images, draw boxes, auto-export. Team collaboration |
| 🌐 **CVAT** | Web-based | Professional tool used by research institutions |
 
**YOLO Annotation Format** (`.txt` file per image):
```
# <class_id>  <center_x>  <center_y>  <width>  <height>
0              0.45         0.32        0.25      0.30
# All values normalized 0–1 (relative to image size)
# class_id = 0 = 'meter'  (only 1 class in this project)
```
 
**Annotation Stats:**
- 📸 **1,000** images annotated
- 🏷️ **~2,400** total bounding boxes drawn
- ⏱️ **~60 minutes** total annotation time
---
 
### Step 3 — Dataset Preparation
 
<img src="screenshots/slide_10.jpg" alt="Step 3 — Dataset Preparation" width="100%" />
<br/>
1,000 annotated images are split into three sets:
 
| Split | Ratio | Images | Role |
|-------|-------|--------|------|
| **Train** | 70% | 700 | Model learns — weights updated every epoch |
| **Val** | 15% | 150 | Monitors overfitting — early stopping based on val mAP |
| **Test** | 15% | 150 | Final unbiased evaluation — never seen during training |
 
> **Key Rule:** Test set is **never used** for any training decisions — only for final reporting. This prevents data leakage and ensures a true generalization metric.
 
```python
pipeline = MeterDetectionPipeline()
splits = pipeline.step3_prepare_dataset()
# Output: train=700, val=150, test=150
# Generates: data/dataset/dataset.yaml
```
 
---
 
### Step 4 — Model Training
 
<img src="screenshots/slide_11.jpg" alt="Step 4 — Model Training" width="100%" />
<br/>
```bash
python yolov5/train.py \
  --img 640 \
  --batch 16 \
  --epochs 50 \
  --data data/dataset/dataset.yaml \
  --weights yolov5s.pt \
  --device 0 \
  --patience 20 \
  --project models \
  --name meter_detection
```
 
**Training Configuration:**
 
| Parameter | Value | Reason |
|-----------|-------|--------|
| Base Model | `yolov5s.pt` (pretrained COCO) | Transfer learning — not from scratch |
| Image Size | `640 × 640 px` | Standard YOLO input — balanced speed/accuracy |
| Batch Size | `8` (reduced from 16) | Optimized to fit GPU memory (CUDA OOM fix) |
| Epochs | `50` | Early stopping (patience=20) prevents overfitting |
| Optimizer | SGD + Weight Decay | L2 regularization prevents weight explosion |
| Device | GPU (CUDA:0) | CPU fallback available — 3× slower |
 
**Training Loss Progression:**
 
| Epoch | Total Loss | Box Loss | Precision | Status |
|-------|-----------|----------|-----------|--------|
| 1/50 | 2.50 | 0.92 | 32% | Learning starts |
| 10/50 | 0.80 | 0.28 | 71% | Improving fast |
| 25/50 | 0.35 | 0.12 | 85% | Converging |
| 50/50 | **0.22** | **0.06** | **95%** | ✅ Best model saved |
 
---
 
### 🧠 Transfer Learning — The Key Technique
 
<img src="screenshots/slide_12.jpg" alt="Transfer Learning" width="100%" />
<br/>
| | ❌ Without Transfer Learning | ✅ With Transfer Learning (Our Approach) |
|--|--|--|
| **Starting Point** | Random weights (knows nothing) | `yolov5s.pt` pretrained on 1.4M COCO images |
| **Images Needed** | 10,000+ minimum | **1,000 images** (sufficient) |
| **Training Time** | 5–7 days on GPU | **~2 hours on RTX 3060** |
| **Achieved mAP** | 70–80% (if enough data) | **0.94 mAP@50** |
| **Risk** | Underfitting, poor generalization | Early layers already know edges, textures |
 
> **Result:** 95% Precision / 0.94 mAP achieved in 2 hours using only 1000 images — **transfer learning makes this possible!**
 
---
 
### Step 5 — Inference & Results
 
<img src="screenshots/slide_13.jpg" alt="Step 5 — Inference & Results" width="100%" />
<br/>
**Inference Pipeline:**
```python
model   = torch.load('best.pt')           # Load trained model
img     = cv2.imread(image_path)          # Load image
img     = cv2.resize(img, (640, 640))     # Resize to YOLO input size
results = model(img, conf=0.5)            # Run detection
boxes   = results[conf >= threshold]      # Filter by confidence
cv2.rectangle(img, (x1,y1),(x2,y2))      # Draw bounding boxes
cv2.imwrite('detected.jpg', img)          # Save output
```
 
**Detection Parameters:**
 
| Parameter | Value | Description |
|-----------|-------|-------------|
| Confidence Threshold | `0.6 (60%)` | Only show detections ≥ 60% confident |
| IOU Threshold (NMS) | `0.45` | Remove duplicate overlapping boxes |
| Inference Speed | `6.5 ms/image` | 152 FPS on RTX 3060 GPU |
| Output Format | `JPG + JSON` | Annotated image + structured data |
 
**REST API Response:**
```json
{
  "detections": [
    { "x1": 102, "y1": 155, "x2": 220, "y2": 280, "conf": 0.96 },
    { "x1": 340, "y1": 88,  "x2": 465, "y2": 205, "conf": 0.91 }
  ],
  "total_meters": 2,
  "processing_ms": 6.5
}
```
 
---
 
## 📁 Project File Structure
 
<img src="screenshots/slide_14.jpg" alt="Project File Structure" width="100%" />
<br/>
```
meter_detection_project/
│
├── 📂 data/
│   ├── videos/                   ← Input MP4/AVI survey videos
│   ├── frames/
│   │   ├── extracted/            ← Step 1 output JPGs (~360 images)
│   │   └── annotated/            ← Step 2 YOLO label .txt files
│   └── dataset/
│       ├── images/train|val|test/ ← Split images
│       ├── labels/train|val|test/ ← Matching YOLO labels
│       └── dataset.yaml           ← YOLOv5 dataset config
│
├── 📂 models/
│   ├── yolov5s.pt                ← Pretrained COCO weights (14 MB)
│   └── meter_detection/
│       └── weights/
│           └── best.pt           ← 🏆 Best trained model checkpoint
│
├── 📂 results/
│   └── detections/               ← Output annotated images + JSON
│
├── 📂 src/
│   ├── config.py                 ← Config class (reads config.json)
│   ├── pipeline.py               ← Core: step1–step5 methods
│   └── utils.py                  ← Helper utilities
│
├── 📂 app/
│   ├── __init__.py
│   └── app.py                    ← Flask REST API + Web UI backend
│
├── 📂 templates/
│   ├── index.html                ← Frontend detection dashboard UI
│   └── login.html                ← Login / Signup page
│
├── 📂 uploads/                   ← Images saved by /api/detect
├── 📂 upload_videos/             ← Videos saved by /upload_video
├── 📂 yolov5/                    ← YOLOv5 submodule (git cloned)
│
├── ⚙️  config.json               ← All settings — single source of truth
├── 📋  requirements.txt          ← 9 Python dependencies
├── 🔧  fix_labels.py             ← Fix annotation class ID mismatches
├── 🗄️  detections.db             ← SQLite results database
│
├── 🚀  run_full_pipeline.py      ← Master runner (all 5 steps interactive)
├── 🔹  run_step_1.py             ← Frame extraction
├── 🔹  run_step_3.py             ← Dataset preparation
├── 🔹  run_step_4.py             ← Model training (calls yolov5/train.py)
├── 🔹  run_step_5.py             ← Inference
└── 🌐  run_flask_app.py          ← Start REST API server (port 5000)
```
 
**Key File Roles:**
 
| File | Purpose |
|------|---------|
| `run_full_pipeline.py` | Master runner — calls all 5 steps in sequence with interactive prompts |
| `src/pipeline.py` | Core logic — contains `step1`–`step5` methods; heart of the project |
| `src/config.py` | Loads `config.json`, provides typed constants (IMG_SIZE, EPOCHS, etc.) |
| `config.json` | Single place to change all settings — no need to touch Python code |
| `run_flask_app.py` | Starts REST API server on port 5000, accepts image uploads for detection |
| `fix_labels.py` | Utility to normalize class IDs if multiple annotation tools caused inconsistencies |
| `requirements.txt` | Lists all 9 Python packages — install with `pip install -r requirements.txt` |
 
---
 
## 🌐 Flask REST API
 
<img src="screenshots/slide_15.jpg" alt="Flask REST API" width="100%" />
<br/>
```bash
# Start the server
python run_flask_app.py
 
# Server is live at: http://localhost:5000
```
 
**Architecture:**
```
CLIENT (Browser / App / TPCODL System)
         │
         │  POST /detect  ← image file
         ▼
   FLASK REST API (run_flask_app.py · Port 5000)
         │
         │  Inference Request
         ▼
   YOLOV5 MODEL (best.pt · PyTorch)
         │
         │  JSON Response with detections
         ▼
   CLIENT receives: { detections, total_meters, processing_ms }
```
 
**API Endpoints:**
 
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/detect` | Upload image → returns detection JSON |
| `POST` | `/api/upload_video` | Upload video for batch processing |
| `GET` | `/api/history` | Fetch last 50 detection results from SQLite |
| `GET` | `/` | Web UI dashboard |
 
**Example cURL:**
```bash
curl -X POST http://localhost:5000/api/detect \
  -F "file=@meter_image.jpg" \
  | python -m json.tool
```
 
**Key Flask Config:**
```python
app.run(
    host='0.0.0.0',       # Listen on ALL interfaces (LAN accessible)
    port=5000,            # HTTP port → http://server-ip:5000
    debug=False,          # Production mode
    use_reloader=False    # Disable reloader (prevents PyTorch double-load)
)
```
 
---
 
## 🖥️ Live Web Interface
 
### Step 1 — Create Account
 
<img src="screenshots/slide_16.jpg" alt="Create Account" width="100%" />
<br/>
### Step 2 — Login
 
<img src="screenshots/slide_17.jpg" alt="Login Page" width="100%" />
<br/>
### Step 3 — Detection Dashboard (Upload Image + Set Confidence)
 
<img src="screenshots/slide_18.jpg" alt="Detection Dashboard" width="100%" />
<br/>
**How to use the dashboard:**
1. 📤 **Upload** an image (JPG/PNG) of a meter or building
2. 🎚️ **Set confidence threshold** (default: 60%)
3. 🔍 **Press Detect** — model runs in milliseconds
4. 📊 **View output** — annotated image with bounding boxes + detection count
### Step 4 — Detection History Log
 
<img src="screenshots/slide_19.jpg" alt="Detection History" width="100%" />
<br/>
- Every detection is automatically saved to **SQLite database**
- Last **50 entries** visible in the history panel
- ⬇️ **Downloadable** as CSV for reporting
### Step 5 — Full System View
 
<img src="screenshots/slide_20.jpg" alt="Full System View" width="100%" />
<br/>
---
 
## 📈 Before vs After — Impact Analysis
 
<img src="screenshots/slide_21.jpg" alt="Impact Analysis" width="100%" />
<br/>
| KPI | 🔴 Before (Manual) | 🟢 After (AI System) | Improvement |
|-----|-------------------|---------------------|-------------|
| ⏱️ **Time per Building** | 40+ hours | 2 hours | ✅ **95% reduction** |
| 💸 **Inspection Cost** | ₹20,000–₹25,000 | ₹2,000 | ✅ **90% savings** |
| 👁️ **Meter Miss Rate** | 5–10% missed | <5% | ✅ **2× fewer misses** |
| 📋 **Scalability** | 1 team, serial | Unlimited parallel | ✅ **Fully scalable** |
| 📄 **Report Generation** | Manual + paper | Auto JSON + SQLite DB | ✅ **100% digital** |
| 🎯 **Detection Accuracy** | ~90% (fatigue affected) | 95%+ consistent | ✅ **+5% accuracy** |
 
---
 
## 🏆 Conclusion
 
<img src="screenshots/slide_22.jpg" alt="Conclusion and Future Scope" width="100%" />
<br/>
**What was achieved:**
 
- ✅ Built a **fully functional end-to-end meter detection system** using YOLOv5
- ✅ Achieved **95% Precision, 96% Recall, 0.94 mAP** — exceeding the 90% target
- ✅ Reduced inspection time by 95%: **40 hours → 2 hours** per building
- ✅ Reduced cost by 90%: **₹25,000 → ₹2,000** per inspection
- ✅ Deployed working **REST API** ready for TPCODL system integration
- ✅ Applied **transfer learning** — trained in 2 hrs using only 1000 images
- ✅ Handled real challenges: CUDA OOM, overfitting, annotation bottleneck
- ✅ System is **production-ready** with Flask API and SQLite results database
---
 
## 🔮 Future Scope
 
| # | Enhancement | Description |
|---|------------|-------------|
| 1 | **Multi-class Detection** | Detect analog, digital, and smart meters separately for better asset management |
| 2 | **Real-time Video Streams** | Connect to CCTV feeds or drones for live continuous monitoring |
| 3 | **Edge Deployment** | Run on Jetson Nano / Raspberry Pi for offline on-site inspections |
| 4 | **Active Learning** | Model flags uncertain detections for human review — reduces annotation by 70% |
| 5 | **Night Vision Support** | Low-light training data + histogram equalization pipeline |
| 6 | **TPCODL System Link** | Directly update asset management database with detected meter locations |
| 7 | **Docker + Cloud Deploy** | Containerize with Docker, deploy on AWS/GCP for scalable multi-site use |
 
---
 
## 🚀 Quick Start
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/YOUR_USERNAME/meter-detection-system.git
cd meter-detection-system
```
 
### 2. Create & Activate Virtual Environment
 
```bash
# Windows
python -m venv venv
venv\Scripts\activate
 
# macOS / Linux
python -m venv venv
source venv/bin/activate
```
 
### 3. Install Dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Clone YOLOv5
 
```bash
git clone https://github.com/ultralytics/yolov5.git
```
 
### 5. Place Your Survey Video
 
```
data/videos/sample_meter_video.mp4
```
 
### 6. Run Full Pipeline (Interactive)
 
```bash
python run_full_pipeline.py
```
 
**Or run individual steps:**
```bash
python run_step_1.py    # Extract frames from video
# → Annotate frames with LabelImg or Roboflow
python run_step_3.py    # Prepare dataset splits
python run_step_4.py    # Train YOLOv5 (~2 hours on GPU)
python run_step_5.py    # Run inference + save results
```
 
### 7. Launch Web Interface
 
```bash
python run_flask_app.py
# Open: http://localhost:5000
```
 
---
 
## ⚙️ Configuration
 
All settings in one file — **`config.json`** — no code changes needed:
 
```json
{
  "project_name": "Meter Detection",
  "version": "1.0.0",
 
  "extraction": {
    "frame_interval": 5,       // Extract every 5th frame
    "format": "jpg"
  },
 
  "training": {
    "img_size": 640,           // YOLOv5 input resolution (px)
    "batch_size": 16,          // Reduce to 8 if you get CUDA OOM error
    "epochs": 50,              // Max training epochs
    "device": 0,               // GPU index (0 = first GPU)
    "patience": 20             // Early stopping patience (epochs)
  },
 
  "inference": {
    "conf_threshold": 0.5,     // Min detection confidence (0.0–1.0)
    "iou_threshold": 0.45      // NMS overlap threshold
  },
 
  "database": {
    "enabled": false,
    "type": "oracle",
    "host": "localhost",
    "port": 1521
  }
}
```
 
---
 
## 🛠️ Troubleshooting
 
| Problem | Fix |
|---------|-----|
| `CUDA Out of Memory` | Reduce `batch_size` from 16 → 8 in `config.json` |
| `No module named torch` | Activate venv and run `pip install -r requirements.txt` |
| `Dataset YAML not found` | Run `python run_step_3.py` before training |
| `Port 5000 already in use` | Kill the existing process or change port in `run_flask_app.py` |
| `Label class mismatch error` | Run `python fix_labels.py` to normalize all class IDs to `0` |
| `Model weights not found` | Ensure `best.pt` exists in `models/meter_detection/weights/` |
| Training accuracy not improving | Check annotations for errors; ensure no data leakage between splits |
 
---
 
## 👤 Author
 
<div align="center">
**Sumit Kumar Sahu**  
B.Tech — Computer Science (Artificial Intelligence & Machine Learning)
 
Internship Project · **TPCODL** (TP Central Odisha Distribution Ltd.) · 2026
 
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YOUR_USERNAME)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_PROFILE)
 
---
 
<img src="screenshots/slide_23.jpg" alt="Thank You" width="80%" />
<br/><br/>
 
**⭐ Found this useful? Star the repository! ⭐**
 
*Built with ❤️ using YOLOv5 · PyTorch · Flask · OpenCV · Python*
 
</div>
 
