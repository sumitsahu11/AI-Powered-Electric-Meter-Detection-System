<div align="center">
<img src="assets/banner.svg" width="100%" alt="Electric Meter Detection System"/>
</div>

<br>

<div align="center">

<a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/></a>
<a href="https://pytorch.org"><img src="https://img.shields.io/badge/PyTorch-2.0.1-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/></a>
<a href="https://github.com/ultralytics/yolov5"><img src="https://img.shields.io/badge/YOLOv5-v7.0.13-00FFFF?style=for-the-badge&logo=github&logoColor=black"/></a>
<a href="https://flask.palletsprojects.com"><img src="https://img.shields.io/badge/Flask-2.3.3-000000?style=for-the-badge&logo=flask&logoColor=white"/></a>
<a href="https://opencv.org"><img src="https://img.shields.io/badge/OpenCV-4.8.1-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/></a>
<img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Production Ready-22c55e?style=for-the-badge"/>

<br><br>

<p><b>Internship Project &nbsp;·&nbsp; TPCODL (TP Central Odisha Distribution Ltd.) &nbsp;·&nbsp; 2026</b><br>
Developed by <b>Sumit Kumar Sahu</b> &nbsp;·&nbsp; B.Tech CS (AI &amp; ML)</p>

</div>

---

## 📋 Table of Contents

- [Executive Summary](#executive-summary)
- [Problem Statement](#problem-statement)
- [Proposed Solution](#proposed-solution)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Pipeline — All 5 Steps](#pipeline--all-5-steps)
- [Transfer Learning](#transfer-learning)
- [Project File Structure](#project-file-structure)
- [Flask REST API](#flask-rest-api)
- [Live Web Interface](#live-web-interface)
- [Impact Analysis](#impact-analysis)
- [Conclusion](#conclusion)
- [Future Scope](#future-scope)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

---

## Executive Summary

<img src="screenshots/slide_03.jpg" width="100%" alt="Executive Summary"/>

<br>

An **end-to-end automated electric meter detection system** powered by **YOLOv5 deep learning** — identifying and precisely locating electric meters in images and videos. Built during an internship at **TPCODL**, this system replaces expensive, error-prone manual field inspections with a fully automated, scalable AI pipeline.

**Objectives:**

- 🎯 Automate detection of electric meters in field survey video footage
- ⏱️ Reduce inspection time from **40+ hours → under 2 hours** per building zone
- 🌐 Deploy as a **REST API** for seamless TPCODL infrastructure integration
- ✅ Achieve minimum 90% detection accuracy — **final result: 95%+ precision**

---

## Problem Statement

<img src="screenshots/slide_04.jpg" width="100%" alt="Problem Statement"/>

<br>

Manual electric meter inspection at TPCODL was **inefficient, expensive, and error-prone**:

| Issue | Old Way | Impact |
|-------|---------|--------|
| ⏱️ Time Inefficiency | 40+ hours / building | Field teams walk every floor, record manually |
| 💸 High Cost | ₹20,000–₹25,000 / inspection | Unsustainable across hundreds of buildings |
| 👁️ Human Error | 5–10% meters missed | Revenue loss and compliance failures |
| 📋 No Scalability | 1 team, serial process | Cannot scale to TPCODL's growing grid |

---

## Proposed Solution

<img src="screenshots/slide_05.jpg" width="100%" alt="Proposed Solution"/>

<br>

A **5-step AI pipeline** transforms raw survey videos into structured detection reports — automatically:

```
Video  -->  Frame Extraction  -->  Annotation  -->  Training  -->  Inference  -->  Results
```

| Step | What Happens | Tool | Time |
|------|-------------|------|------|
| **1** | Extract frames from video | OpenCV | ~5 min |
| **2** | Manually annotate meters | LabelImg / Roboflow | ~60 min |
| **3** | Prepare train/val/test splits | Python | ~2 min |
| **4** | Train YOLOv5 model | YOLOv5 + PyTorch | ~120 min |
| **5** | Run inference + save results | PyTorch | ~5 min |

---

## Technology Stack

<img src="screenshots/slide_06.jpg" width="100%" alt="Technology Stack"/>

<br>

| Technology | Version | Role |
|-----------|---------|------|
| Python | `3.10+` | Core language |
| YOLOv5 | `v7.0.13` | Object detection — 152 FPS, 14 MB model |
| PyTorch | `2.0.1` | Deep learning framework + GPU acceleration |
| OpenCV | `4.8.1` | Frame extraction + image manipulation |
| Flask | `2.3.3` | Lightweight REST API server |
| NumPy | `1.24.3` | Numerical computing + matrix operations |
| Pillow | `10.0.1` | Image load / save / transform |
| TorchVision | `0.15.2` | Vision transforms + dataset loaders |
| Flask-CORS | `4.0.0` | Cross-origin API access for browser clients |

---

## System Architecture

<img src="screenshots/slide_07.jpg" width="100%" alt="System Architecture"/>

<br>

```
[VIDEO INPUT]         data/videos/
      |
      v
[STEP 1]  Frame Extraction  (OpenCV)       -->  data/frames/extracted/       ~5 min
      |
      v
[STEP 2]  Manual Annotation (LabelImg)     -->  data/frames/annotated/       ~60 min
      |
      v
[STEP 3]  Dataset Preparation (Python)     -->  data/dataset/  70/15/15      ~2 min
      |
      v
[STEP 4]  YOLOv5 Training (PyTorch)        -->  models/meter_detection/      ~120 min
      |
      v
[STEP 5]  Inference and Results            -->  results/ + SQLite + REST API
```

---

## Pipeline — All 5 Steps

---

### Step 1 — Frame Extraction

<img src="screenshots/slide_08.jpg" width="100%" alt="Step 1 Frame Extraction"/>

<br>

```python
pipeline = MeterDetectionPipeline()
num_frames = pipeline.step1_extract_frames()
# Output: ~360 JPG images saved to data/frames/extracted/
```

A 60-second video at 30 FPS = 1,800 frames. Sampling every 5th frame gives ~360 images — enough coverage while saving **80% disk space**.

```
survey.mp4  -->  cv2.VideoCapture()  -->  frame_count % 5 == 0  -->  frame_0001.jpg ... frame_0360.jpg
```

---

### Step 2 — Data Annotation

<img src="screenshots/slide_09.jpg" width="100%" alt="Step 2 Data Annotation"/>

<br>

Drawing bounding boxes on every frame to teach the AI where meters are.

| Tool | Type | Notes |
|------|------|-------|
| **LabelImg** | Desktop, open-source | Primary tool — saves in YOLO `.txt` format |
| **Roboflow** | Cloud-based | Upload, annotate, auto-export, team support |
| **CVAT** | Web-based | Professional-grade annotation platform |

**YOLO label format** — one `.txt` per image:

```
class_id   center_x   center_y   width   height
0          0.45       0.32       0.25    0.30
```

All values normalized 0–1. `class_id = 0 = meter`.

**Stats:** 1,000 images · ~2,400 bounding boxes · ~60 minutes annotation time

---

### Step 3 — Dataset Preparation

<img src="screenshots/slide_10.jpg" width="100%" alt="Step 3 Dataset Preparation"/>

<br>

| Split | Ratio | Images | Role |
|-------|-------|--------|------|
| **Train** | 70% | 700 | Model learns — weights updated each epoch |
| **Val** | 15% | 150 | Monitors overfitting — early stopping signal |
| **Test** | 15% | 150 | Final evaluation — never seen during training |

```python
splits = pipeline.step3_prepare_dataset()
# Generates: data/dataset/dataset.yaml  (required by YOLOv5)
```

---

### Step 4 — Model Training

<img src="screenshots/slide_11.jpg" width="100%" alt="Step 4 Model Training"/>

<br>

```bash
python yolov5/train.py \
  --img 640 --batch 16 --epochs 50 \
  --data data/dataset/dataset.yaml \
  --weights yolov5s.pt \
  --device 0 --patience 20 \
  --project models --name meter_detection
```

**Training Progression:**

| Epoch | Total Loss | Precision | Status |
|-------|-----------|-----------|--------|
| 1 / 50 | 2.50 | 32% | Learning starts |
| 10 / 50 | 0.80 | 71% | Rapid improvement |
| 25 / 50 | 0.35 | 85% | Converging |
| **50 / 50** | **0.22** | **95%** | ✅ Best model saved |

---

## Transfer Learning

<img src="screenshots/slide_12.jpg" width="100%" alt="Transfer Learning"/>

<br>

| | Without Transfer Learning | With Transfer Learning |
|--|--|--|
| Starting weights | Random — knows nothing | `yolov5s.pt` pretrained on 1.4M COCO images |
| Images needed | 10,000+ minimum | **1,000 images** |
| Training time | 5–7 days | **~2 hours on RTX 3060** |
| Achieved mAP | 70–80% | **0.94 mAP@50** |

---

### Step 5 — Inference and Results

<img src="screenshots/slide_13.jpg" width="100%" alt="Step 5 Inference and Results"/>

<br>

```python
model   = torch.load('models/meter_detection/weights/best.pt')
img     = cv2.resize(cv2.imread(image_path), (640, 640))
results = model(img, conf=0.5)
# Draw bounding boxes and save output image
```

| Parameter | Value |
|-----------|-------|
| Confidence Threshold | `0.6` — only show detections >= 60% |
| IOU / NMS Threshold | `0.45` — remove duplicate boxes |
| Inference Speed | `6.5 ms / image` — 152 FPS on GPU |
| Output | Annotated JPG + JSON response |

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

## Project File Structure

<img src="screenshots/slide_14.jpg" width="100%" alt="Project File Structure"/>

<br>

```
meter_detection_project/
|
+-- data/
|   +-- videos/                   <-- Input MP4/AVI survey videos
|   +-- frames/
|   |   +-- extracted/            <-- Step 1 JPG output (~360 images)
|   |   +-- annotated/            <-- Step 2 YOLO label .txt files
|   +-- dataset/
|       +-- images/train|val|test/
|       +-- labels/train|val|test/
|       +-- dataset.yaml
|
+-- models/
|   +-- yolov5s.pt                <-- Pretrained COCO weights
|   +-- meter_detection/
|       +-- weights/
|           +-- best.pt           <-- Your trained model
|
+-- results/detections/           <-- Output annotated images + JSON
+-- src/config.py                 <-- Config class
+-- src/pipeline.py               <-- Core step1-step5 logic
+-- app/app.py                    <-- Flask REST API backend
+-- templates/index.html          <-- Web UI dashboard
+-- templates/login.html          <-- Login / Signup page
+-- config.json                   <-- All settings (single source of truth)
+-- requirements.txt              <-- 9 Python dependencies
+-- fix_labels.py                 <-- Fix annotation class ID mismatches
+-- detections.db                 <-- SQLite results database
+-- run_full_pipeline.py          <-- Master runner (all 5 steps)
+-- run_step_1.py / 3 / 4 / 5    <-- Individual step runners
+-- run_flask_app.py              <-- Start server on port 5000
```

---

## Flask REST API

<img src="screenshots/slide_15.jpg" width="100%" alt="Flask REST API"/>

<br>

```bash
python run_flask_app.py
# Live at: http://localhost:5000
```

**Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/detect` | Upload image → bounding boxes + confidence JSON |
| `POST` | `/api/upload_video` | Upload video for batch processing |
| `GET` | `/api/history` | Last 50 detection records from SQLite |
| `GET` | `/` | Web UI dashboard |

```bash
curl -X POST http://localhost:5000/api/detect \
  -F "file=@meter_photo.jpg" | python -m json.tool
```

---

## Live Web Interface

### Create Account

<img src="screenshots/slide_16.jpg" width="100%" alt="Create Account"/>

<br>

### Login

<img src="screenshots/slide_17.jpg" width="100%" alt="Login"/>

<br>

### Detection Dashboard

<img src="screenshots/slide_18.jpg" width="100%" alt="Detection Dashboard"/>

<br>

1. Upload a JPG or PNG photo
2. Set confidence threshold (default 60%)
3. Press Detect — runs in 6.5 ms
4. View annotated output with bounding boxes and count

### Detection History

<img src="screenshots/slide_19.jpg" width="100%" alt="Detection History"/>

<br>

### Full System View

<img src="screenshots/slide_20.jpg" width="100%" alt="Full System"/>

<br>

---

## Impact Analysis

<img src="screenshots/slide_21.jpg" width="100%" alt="Impact Analysis"/>

<br>

| KPI | Before (Manual) | After (AI) | Improvement |
|-----|----------------|------------|-------------|
| Time per Building | 40+ hours | 2 hours | ✅ 95% faster |
| Inspection Cost | ₹25,000 | ₹2,000 | ✅ 90% savings |
| Meter Miss Rate | 5–10% | less than 5% | ✅ 2x fewer misses |
| Scalability | 1 team, serial | Unlimited parallel | ✅ Fully scalable |
| Reporting | Manual + paper | Auto JSON + SQLite | ✅ 100% digital |
| Accuracy | ~90% (fatigue) | 95%+ consistent | ✅ +5% accuracy |

---

## Conclusion

<img src="screenshots/slide_22.jpg" width="100%" alt="Conclusion"/>

<br>

- ✅ Fully functional end-to-end meter detection system using YOLOv5
- ✅ **95% Precision · 96% Recall · 0.94 mAP** — exceeded the 90% target
- ✅ Inspection time cut by 95% — 40 hours → 2 hours per building
- ✅ Cost cut by 90% — ₹25,000 → ₹2,000 per inspection
- ✅ Working REST API ready for TPCODL system integration
- ✅ Transfer learning — trained in 2 hours with only 1,000 images
- ✅ Production-ready with Flask API, SQLite logging, and full web UI

---

## Future Scope

| # | Enhancement | Description |
|---|------------|-------------|
| 1 | Multi-class Detection | Detect analog, digital, and smart meters separately |
| 2 | Real-time Video Streams | Connect to CCTV or drone feeds for live monitoring |
| 3 | Edge Deployment | Run on Jetson Nano / Raspberry Pi for offline inspections |
| 4 | Active Learning | Model flags uncertain detections — reduces annotation by 70% |
| 5 | Night Vision | Low-light training data + histogram equalization |
| 6 | TPCODL Integration | Write meter locations directly to asset management DB |
| 7 | Docker + Cloud | Deploy on AWS / GCP for scalable multi-site production |

---

## Quick Start

### 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/meter-detection-system.git
cd meter-detection-system
```

### 2 — Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

### 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 — Clone YOLOv5

```bash
git clone https://github.com/ultralytics/yolov5.git
```

### 5 — Run Full Pipeline

```bash
python run_full_pipeline.py
```

Or step by step:

```bash
python run_step_1.py    # Extract frames
                        # Annotate with LabelImg or Roboflow
python run_step_3.py    # Prepare dataset splits
python run_step_4.py    # Train model (~2 hrs on GPU)
python run_step_5.py    # Inference + save results
```

### 6 — Launch Web Interface

```bash
python run_flask_app.py
# Open: http://localhost:5000
```

---

## Configuration

All settings in `config.json` — no Python code changes needed:

```json
{
  "extraction": { "frame_interval": 5, "format": "jpg" },
  "training": {
    "img_size": 640,
    "batch_size": 16,
    "epochs": 50,
    "device": 0,
    "patience": 20
  },
  "inference": {
    "conf_threshold": 0.5,
    "iou_threshold": 0.45
  }
}
```

| Key | Default | When to change |
|-----|---------|----------------|
| `frame_interval` | `5` | Lower = more frames = more training data |
| `batch_size` | `16` | Reduce to `8` if you get CUDA Out of Memory error |
| `epochs` | `50` | Increase if accuracy is not yet sufficient |
| `conf_threshold` | `0.5` | Raise to reduce false positives |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| CUDA Out of Memory | Reduce `batch_size` to `8` in `config.json` |
| No module named torch | Activate venv then `pip install -r requirements.txt` |
| Dataset YAML not found | Run `python run_step_3.py` before training |
| Port 5000 in use | Kill existing process or change port in `run_flask_app.py` |
| Label class mismatch | Run `python fix_labels.py` to normalize all class IDs to `0` |
| Weights not found | Check `models/meter_detection/weights/best.pt` exists |

---

## Author

<div align="center">

<h3>Sumit Kumar Sahu</h3>
<p>B.Tech — Computer Science (Artificial Intelligence &amp; Machine Learning)</p>
<p>Internship Project &nbsp;·&nbsp; <b>TPCODL</b> &nbsp;·&nbsp; 2026</p>

<a href="https://github.com/YOUR_USERNAME">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
</a>
&nbsp;
<a href="https://linkedin.com/in/YOUR_PROFILE">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<br><br>

<img src="screenshots/slide_23.jpg" width="75%" alt="Thank You"/>

<br><br>

<b>⭐ Found this useful? Please star the repository! ⭐</b>

<br>

<i>Built with ❤️ using YOLOv5 · PyTorch · Flask · OpenCV · Python</i>

</div>
