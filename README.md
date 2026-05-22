


<div align="center">


<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0.1-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![YOLOv5](https://img.shields.io/badge/YOLOv5-v7.0.13-00FFFF?style=for-the-badge&logo=github&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-2.3.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.1-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

<br/>

![Precision](https://img.shields.io/badge/Precision-95%25+-success?style=flat-square)
![Speed](https://img.shields.io/badge/Speed-152%20FPS-blueviolet?style=flat-square)
![mAP](https://img.shields.io/badge/mAP@50-0.94-orange?style=flat-square)
![Model Size](https://img.shields.io/badge/Model%20Size-14%20MB-blue?style=flat-square)
![Cost Reduction](https://img.shields.io/badge/Cost%20Reduction-90%25-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

<br/>

**Developed by [Sumit Kumar Sahu](https://github.com/sumitkumarsahu) — B.Tech CS (AI & ML)**

*Internship Project — TPCODL Field Operations Automation — 2026*

</div>

---

## 📌 Table of Contents

| # | Section |
|---|---------|
| 1 | [🧠 Project Overview](#-project-overview) |
| 2 | [❗ Problem Statement](#-problem-statement) |
| 3 | [💡 Proposed Solution](#-proposed-solution) |
| 4 | [🏆 Key Results](#-key-results) |
| 5 | [🛠️ Technology Stack](#️-technology-stack) |
| 6 | [🏗️ System Architecture](#️-system-architecture) |
| 7 | [📁 Project Structure](#-project-structure) |
| 8 | [🚀 Getting Started](#-getting-started) |
| 9 | [🔄 5-Step Pipeline](#-5-step-pipeline) |
| 10 | [🌐 Flask REST API](#-flask-rest-api) |
| 11 | [📊 Model Performance](#-model-performance) |
| 12 | [📈 Business Impact](#-business-impact) |
| 13 | [⚠️ Challenges & Solutions](#️-challenges--solutions) |
| 14 | [🔮 Future Scope](#-future-scope) |
| 15 | [🤝 Contributing](#-contributing) |
| 16 | [📄 License](#-license) |

---

## 🧠 Project Overview

> **An end-to-end AI pipeline that automatically detects electric meters in field-survey videos — deployed as a production REST API for TPCODL infrastructure integration.**

This project was built as an internship deliverable for **TPCODL (Tata Power Central Odisha Distribution Limited)** to eliminate manual meter inspection. The system processes raw survey videos, extracts frames, trains a custom YOLOv5 deep learning model, and exposes a web interface + REST API for real-world deployment.

The entire pipeline — from raw video to annotated detections — runs in under **2 hours**, compared to **40+ hours** of manual inspection per building zone.

---

## ❗ Problem Statement

Manual electric meter inspection at TPCODL was:

| Challenge | Impact |
|-----------|--------|
| ⏱ **Time Inefficiency** | 40+ hours per building zone |
| 💸 **High Cost** | ₹20,000–25,000 per inspection |
| 👁 **Human Error** | 5–10% of meters missed due to fatigue |
| 📋 **Zero Scalability** | Serial process; cannot run across multiple buildings in parallel |

These inefficiencies caused **revenue loss**, **compliance failures**, and **operational bottlenecks** across TPCODL's growing grid.

---

## 💡 Proposed Solution

A **5-step AI-powered pipeline** that goes from raw video to automated detection reports:

```
🎥 Video Input
    │
    ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Step 1         │────▶│  Step 2         │────▶│  Step 3         │
│  Frame          │     │  Data           │     │  Dataset        │
│  Extraction     │     │  Annotation     │     │  Preparation    │
│  (OpenCV)       │     │  (LabelImg)     │     │  (Python)       │
│  ~5 min         │     │  ~60 min        │     │  ~2 min         │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
                                        ┌─────────────────────────┐
                                        │  Step 4                 │
                                        │  Model Training         │
                                        │  (YOLOv5 + Transfer     │
                                        │   Learning) ~120 min    │
                                        └─────────────────────────┘
                                                        │
                                                        ▼
                                        ┌─────────────────────────┐
                                        │  Step 5                 │
                                        │  Inference & Results    │
                                        │  (152 FPS, JSON + DB)   │
                                        └─────────────────────────┘
                                                        │
                                                        ▼
                                 📊 Detections | Bounding Boxes | Reports
```

---

## 🏆 Key Results

<div align="center">

| Metric | Value |
|--------|-------|
| 🎯 **Precision** | **95%+** |
| 📡 **Recall** | **96%** |
| 📐 **mAP@50** | **0.94** |
| ⚡ **GPU Inference Speed** | **152 FPS (6.5 ms/image)** |
| 📦 **Model Size** | **14 MB** |
| 🕒 **Training Time** | **~2 hours (RTX 3060)** |
| 🖼️ **Training Images** | **1,000** |

</div>

---

## 🛠️ Technology Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    TECHNOLOGY STACK                         │
├──────────────────┬──────────────────────────────────────────┤
│ Language         │ Python 3.10+                             │
│ Detection Model  │ YOLOv5s v7.0.13 (transfer learning)     │
│ Deep Learning    │ PyTorch 2.0.1 + TorchVision 0.15.2      │
│ Computer Vision  │ OpenCV 4.8.1                             │
│ API Framework    │ Flask 2.3.3 + Flask-CORS 4.0.0          │
│ Image Processing │ Pillow 10.0.1                            │
│ Numerical Ops    │ NumPy 1.24.3                             │
│ Database         │ SQLite (detections.db)                   │
│ Annotation Tools │ LabelImg (primary), Roboflow, CVAT       │
│ GPU Acceleration │ CUDA (CPU fallback available)            │
└──────────────────┴──────────────────────────────────────────┘
```

---

## 🏗️ System Architecture

### Flask REST API Flow

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   CLIENT (Browser / TPCODL System / Mobile App)           │
│                │                                           │
│                │  POST /detect  (image file)               │
│                ▼                                           │
│   ┌─────────────────────────┐                             │
│   │    Flask REST API       │  ← run_flask_app.py         │
│   │    Port: 5000           │  ← app/app.py               │
│   └────────────┬────────────┘                             │
│                │  inference request                        │
│                ▼                                           │
│   ┌─────────────────────────┐                             │
│   │    YOLOv5 Model         │  ← models/best.pt           │
│   │    (PyTorch + CUDA)     │  ← 14 MB, 152 FPS           │
│   └────────────┬────────────┘                             │
│                │                                           │
│                ▼                                           │
│   JSON Response:                                           │
│   { "detections": [...], "total_meters": N,               │
│     "processing_ms": 6.5 }                               │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
meter_detection_project/
│
├── 📂 data/
│   ├── 📂 videos/                  ← Input MP4/AVI survey videos
│   ├── 📂 frames/
│   │   ├── extracted/              ← Step 1 output: extracted JPG frames
│   │   └── annotated/              ← Step 2 output: YOLO .txt label files
│   └── 📂 dataset/
│       ├── images/
│       │   ├── train/              ← 700 training images (70%)
│       │   ├── val/                ← 150 validation images (15%)
│       │   └── test/               ← 150 test images (15%)
│       ├── labels/
│       │   ├── train/
│       │   ├── val/
│       │   └── test/
│       └── dataset.yaml            ← YOLO dataset config
│
├── 📂 models/
│   ├── yolov5s.pt                  ← Pretrained COCO weights (14 MB)
│   └── 📂 meter_detection/
│       └── weights/
│           └── best.pt             ← Your trained model (best checkpoint)
│
├── 📂 results/
│   └── detections/                 ← Output annotated images
│
├── 📂 src/
│   ├── config.py                   ← Config class (loads config.json)
│   ├── pipeline.py                 ← Core pipeline (step1–step5 methods)
│   └── utils.py                    ← Helper utilities
│
├── 📂 app/
│   ├── __init__.py
│   └── app.py                      ← Flask app factory + REST API routes
│
├── 📂 templates/
│   ├── index.html                  ← Detection dashboard UI
│   └── login.html                  ← Login / Signup page
│
├── 📂 uploads/                     ← Images uploaded via /api/detect
├── 📂 upload_videos/               ← Videos uploaded via /upload_video
├── 📂 yolov5/                      ← YOLOv5 submodule / library
│
├── run_step_1.py                   ← Frame extraction runner
├── run_step_2.py                   ← (Annotation — manual step)
├── run_step_3.py                   ← Dataset preparation runner
├── run_step_4.py                   ← Model training runner
├── run_step_5.py                   ← Inference runner
├── run_full_pipeline.py            ← Master runner (all 5 steps)
├── run_flask_app.py                ← Start the REST API server
├── fix_labels.py                   ← Fix annotation class ID mismatches
├── show_users.py                   ← View registered users (debug)
├── test_torch_only.py              ← Verify PyTorch install
│
├── detections.db                   ← SQLite database (detection history)
├── config.json                     ← All project settings (single source)
├── requirements.txt                ← All 9 Python dependencies
└── .env                            ← Environment variables (Flask config)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- NVIDIA GPU with CUDA (optional but recommended — CPU fallback available)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/meter-detection-project.git
cd meter-detection-project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify PyTorch Installation

```bash
python test_torch_only.py
# Expected: torch version: 2.0.1 | rand: tensor([...])
```

### 5. Add Your Videos

Place your survey `.mp4` / `.avi` videos inside:

```
data/videos/
```

---

## 🔄 5-Step Pipeline

Run each step sequentially, or use the master runner:

```bash
# Run everything at once (with interactive prompts)
python run_full_pipeline.py
```

Or run steps individually:

### Step 1 — Frame Extraction

```bash
python run_step_1.py
```

> Extracts every 5th frame from input videos using OpenCV. A 60-second video at 30 FPS → ~360 JPG images saved to `data/frames/extracted/`.

### Step 2 — Data Annotation *(manual)*

Use **LabelImg** to annotate meters with bounding boxes:

```bash
pip install labelImg
labelImg data/frames/extracted/ data/frames/annotated/
```

YOLO annotation format (saved per image as `.txt`):

```
# <class_id>  <center_x>  <center_y>  <width>  <height>
0              0.45        0.32        0.25     0.30
```

> Alternatively use [Roboflow](https://roboflow.com) for cloud-based annotation with auto-export.

### Step 3 — Dataset Preparation

```bash
python run_step_3.py
```

> Splits annotated frames into **70% Train / 15% Val / 15% Test** and generates `dataset.yaml` for YOLO.

### Step 4 — Model Training

```bash
python run_step_4.py
```

> Trains YOLOv5s using transfer learning from pretrained COCO weights. Training config from `config.json`:

```json
"training": {
    "img_size": 640,
    "batch_size": 16,
    "epochs": 50,
    "device": 0,
    "patience": 20
}
```

**Training progression:**

| Epoch | Total Loss | Precision | Status |
|-------|------------|-----------|--------|
| 1/50  | 2.50       | 32%       | Learning starts |
| 10/50 | 0.80       | 71%       | Improving fast |
| 25/50 | 0.35       | 85%       | Converging |
| 50/50 | 0.22       | **95%**   | ✅ Best model saved |

### Step 5 — Inference & Results

```bash
python run_step_5.py
```

> Runs the trained `best.pt` model on the test set. Outputs annotated images + JSON detection data to `results/detections/`.

---

## 🌐 Flask REST API

### Start the Server

```bash
python run_flask_app.py
```

> Server starts at `http://localhost:5000`

### Environment Config (`.env`)

```env
FLASK_ENV=development
FLASK_APP=run_flask_app.py
API_HOST=0.0.0.0
API_PORT=5000
MODEL_PATH=models/meter_detection/weights/best.pt
DEVICE=cuda
MAX_FILE_SIZE_MB=50
```

### API Endpoint

**`POST /detect`** — Upload an image, get back detections.

```bash
curl -X POST http://localhost:5000/detect \
     -F "file=@your_image.jpg"
```

**Response:**

```json
{
  "detections": [
    {"x1": 102, "y1": 155, "x2": 220, "y2": 280, "conf": 0.96},
    {"x1": 340, "y1": 88,  "x2": 465, "y2": 205, "conf": 0.91}
  ],
  "total_meters": 2,
  "processing_ms": 6.5
}
```

### Web UI Features

| Feature | Description |
|---------|-------------|
| 🔐 Login / Signup | User authentication page |
| 📤 Image Upload | Drag and drop or browse image files |
| 🎚️ Confidence Control | Adjustable confidence threshold slider |
| 🖼️ Live Detection | Annotated output with bounding boxes |
| 📋 Detection History | Last 50 detection results with timestamps |
| ⬇️ Download History | Export detection log as CSV/JSON |

---

## 📊 Model Performance

### Final Metrics on Test Set

```
┌─────────────────────────────────────────────┐
│           MODEL EVALUATION RESULTS          │
├─────────────────┬───────────────────────────┤
│ Precision       │  95%+                     │
│ Recall          │  96%                      │
│ mAP@50          │  0.94                     │
│ Inference Time  │  6.5 ms/image             │
│ FPS (GPU)       │  152 FPS (RTX 3060)       │
│ Model Size      │  14 MB                    │
│ Conf Threshold  │  0.60                     │
│ IOU Threshold   │  0.45 (NMS)               │
└─────────────────┴───────────────────────────┘
```

### Transfer Learning — Why It Works

| Aspect | Without TL | With Transfer Learning (Ours) |
|--------|-----------|-------------------------------|
| Starting point | Random weights | YOLOv5s.pt (1.4M COCO images) |
| Images needed | 10,000+ | **1,000** |
| Training time | 5–7 days | **~2 hours** |
| Expected mAP | 70–80% | **0.94** |

---

## 📈 Business Impact

```
BEFORE  ──────────────────────────────────  AFTER
─────────────────────────────────────────────────
⏱  Time/Building   40+ hours    →    2 hours    (95% reduction)
💰  Cost/Inspect  Rs.25,000     →   Rs.2,000    (90% savings)
👁  Miss Rate      5–10%        →   < 5%        (2x fewer misses)
📊  Accuracy       ~90%         →   95%+        (+5% gain)
📋  Reports        Manual paper →   Auto JSON   (100% digital)
🔁  Scalability    1 team       →   Unlimited   (fully parallel)
```

> **ROI Positive after just 2 buildings inspected.**

---

## ⚠️ Challenges & Solutions

| Challenge | Solution Applied |
|-----------|-----------------|
| 🔴 CUDA Out-of-Memory during training | Reduced batch size from 16 to 8 |
| 🔴 Multiple annotation class IDs from different tools | `fix_labels.py` normalizes all class IDs to `0` |
| 🔴 Model overfitting on small dataset (1000 images) | Early stopping (patience=20) + SGD + weight decay |
| 🔴 PyTorch import conflicts at startup | Moved `import torch` to top of all entry scripts |
| 🔴 Annotation bottleneck with manual labeling | Supplemented LabelImg with Roboflow for speed |

---

## 🔮 Future Scope

```
1. 🏷️  Multi-class Detection    — Analog / Digital / Smart meter types
2. 📡  Real-time Video Stream   — Live CCTV / drone feed integration
3. 🤖  Edge Deployment          — Jetson Nano / Raspberry Pi for offline use
4. 🧠  Active Learning          — Model flags uncertain detections for review
5. 🌙  Night Vision Support     — Low-light images + histogram equalization
6. 🔗  TPCODL System Link       — Direct asset management DB integration
7. 🐳  Docker + Cloud Deploy    — AWS / GCP containerized deployment
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

```bash
# Fork the repo
git fork https://github.com/YOUR_USERNAME/meter-detection-project

# Create your feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m "feat: add amazing feature"

# Push to the branch
git push origin feature/amazing-feature

# Open a Pull Request
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ by Sumit Kumar Sahu**

*B.Tech Computer Science (AI & ML) | Internship Project 2026*

*Developed for TPCODL Field Operations Automation*

</div>
