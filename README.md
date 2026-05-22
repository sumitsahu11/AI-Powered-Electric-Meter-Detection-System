<svg width="860" height="300" viewBox="0 0 860 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Electric Meter Detection System</title>
  <desc>AI-powered automated meter detection using YOLOv5 — 95% precision, 152 FPS, 0.94 mAP</desc>
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0a14"/>
      <stop offset="55%" stop-color="#0f0c29"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#e0e7ff"/>
      <stop offset="42%" stop-color="#a5b4fc"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0a0a14" stop-opacity="1"/>
      <stop offset="30%" stop-color="#6366f1" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#06b6d4" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#0a0a14" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="statBar" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#a5b4fc" stop-opacity="0.09"/>
      <stop offset="100%" stop-color="#06b6d4" stop-opacity="0.04"/>
    </linearGradient>
    <linearGradient id="orb1g" cx="50%" cy="50%" r="50%" fx="50%" fy="50%" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#6366f1" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="orb2g" cx="50%" cy="50%" r="50%" fx="50%" fy="50%" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#06b6d4" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="orb3g" cx="50%" cy="50%" r="50%" fx="50%" fy="50%" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#a78bfa" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#a78bfa" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="clip"><rect width="860" height="300" rx="14"/></clipPath>
  </defs>

  <rect width="860" height="300" rx="14" fill="url(#bg)"/>
  <g clip-path="url(#clip)">

    <!-- Grid -->
    <g stroke="#6366f1" stroke-opacity="0.07" stroke-width="0.5">
      <line x1="0" y1="50" x2="860" y2="50"/>
      <line x1="0" y1="100" x2="860" y2="100"/>
      <line x1="0" y1="150" x2="860" y2="150"/>
      <line x1="0" y1="200" x2="860" y2="200"/>
      <line x1="0" y1="250" x2="860" y2="250"/>
      <line x1="86" y1="0" x2="86" y2="300"/>
      <line x1="172" y1="0" x2="172" y2="300"/>
      <line x1="258" y1="0" x2="258" y2="300"/>
      <line x1="344" y1="0" x2="344" y2="300"/>
      <line x1="430" y1="0" x2="430" y2="300"/>
      <line x1="516" y1="0" x2="516" y2="300"/>
      <line x1="602" y1="0" x2="602" y2="300"/>
      <line x1="688" y1="0" x2="688" y2="300"/>
      <line x1="774" y1="0" x2="774" y2="300"/>
    </g>

    <!-- Glow orbs -->
    <ellipse cx="110" cy="70" rx="220" ry="170" fill="url(#orb1g)"/>
    <ellipse cx="790" cy="250" rx="180" ry="140" fill="url(#orb2g)"/>
    <ellipse cx="480" cy="145" rx="140" ry="110" fill="url(#orb3g)"/>

    <!-- Detection boxes (right) -->
    <rect x="706" y="46" width="54" height="40" rx="2" fill="none" stroke="#06b6d4" stroke-width="1.2" stroke-opacity="0.55"/>
    <text x="708" y="42" font-family="monospace" font-size="8" fill="#06b6d4" fill-opacity="0.75">meter 0.96</text>
    <rect x="730" y="108" width="46" height="33" rx="2" fill="none" stroke="#06b6d4" stroke-width="1.1" stroke-opacity="0.4"/>
    <text x="732" y="104" font-family="monospace" font-size="8" fill="#06b6d4" fill-opacity="0.55">meter 0.91</text>
    <rect x="706" y="175" width="58" height="42" rx="2" fill="none" stroke="#a5b4fc" stroke-width="1.1" stroke-opacity="0.38"/>
    <text x="708" y="171" font-family="monospace" font-size="8" fill="#a5b4fc" fill-opacity="0.5">meter 0.94</text>

    <!-- Dot accents -->
    <circle cx="676" cy="58"  r="2"   fill="#6366f1" fill-opacity="0.55"/>
    <circle cx="798" cy="88"  r="1.5" fill="#06b6d4" fill-opacity="0.45"/>
    <circle cx="754" cy="158" r="2.5" fill="#a78bfa" fill-opacity="0.35"/>
    <circle cx="818" cy="202" r="1.5" fill="#6366f1" fill-opacity="0.4"/>
    <circle cx="656" cy="228" r="2"   fill="#06b6d4" fill-opacity="0.32"/>
    <circle cx="78"  cy="238" r="1.5" fill="#6366f1" fill-opacity="0.3"/>
    <circle cx="38"  cy="178" r="2"   fill="#06b6d4" fill-opacity="0.28"/>
    <circle cx="52"  cy="108" r="1.5" fill="#a78bfa" fill-opacity="0.3"/>

    <!-- Corner brackets -->
    <path d="M18 30 L18 14 L34 14" fill="none" stroke="#6366f1" stroke-opacity="0.85" stroke-width="1.8" stroke-linecap="round"/>
    <path d="M842 30 L842 14 L826 14" fill="none" stroke="#06b6d4" stroke-opacity="0.85" stroke-width="1.8" stroke-linecap="round"/>
    <path d="M18 270 L18 286 L34 286" fill="none" stroke="#06b6d4" stroke-opacity="0.85" stroke-width="1.8" stroke-linecap="round"/>
    <path d="M842 270 L842 286 L826 286" fill="none" stroke="#6366f1" stroke-opacity="0.85" stroke-width="1.8" stroke-linecap="round"/>

    <!-- Eyebrow label -->
    <text x="390" y="50" font-family="monospace" font-size="10" fill="#6366f1" fill-opacity="0.88" text-anchor="middle" letter-spacing="3.5">INTERNSHIP PROJECT · TPCODL · 2026</text>
    <rect x="195" y="56" width="390" height="0.7" fill="url(#lineGrad)"/>

    <!-- Main title -->
    <text x="390" y="118" font-family="Arial Black, Arial, sans-serif" font-size="48" font-weight="900" fill="url(#titleGrad)" text-anchor="middle" letter-spacing="-2">Electric Meter</text>
    <text x="390" y="170" font-family="Arial Black, Arial, sans-serif" font-size="48" font-weight="900" fill="url(#titleGrad)" text-anchor="middle" letter-spacing="-2">Detection System</text>

    <!-- Subtitle -->
    <text x="390" y="193" font-family="monospace" font-size="11" fill="#a5b4fc" fill-opacity="0.6" text-anchor="middle" letter-spacing="0.8">automated ai pipeline · yolov5 + pytorch · flask rest api</text>

    <!-- Stats bar -->
    <rect x="58" y="210" width="584" height="62" rx="8" fill="url(#statBar)" stroke="#6366f1" stroke-opacity="0.2" stroke-width="0.8"/>
    <line x1="175" y1="222" x2="175" y2="260" stroke="#6366f1" stroke-opacity="0.2" stroke-width="0.8"/>
    <line x1="292" y1="222" x2="292" y2="260" stroke="#6366f1" stroke-opacity="0.2" stroke-width="0.8"/>
    <line x1="409" y1="222" x2="409" y2="260" stroke="#6366f1" stroke-opacity="0.2" stroke-width="0.8"/>
    <line x1="526" y1="222" x2="526" y2="260" stroke="#6366f1" stroke-opacity="0.2" stroke-width="0.8"/>

    <!-- Stat values -->
    <text x="116" y="240" font-family="monospace" font-size="21" font-weight="700" fill="#a5b4fc" text-anchor="middle">95%+</text>
    <text x="116" y="257" font-family="monospace" font-size="8.5" fill="#6366f1" fill-opacity="0.7" text-anchor="middle" letter-spacing="1.5">PRECISION</text>

    <text x="233" y="240" font-family="monospace" font-size="21" font-weight="700" fill="#67e8f9" text-anchor="middle">152</text>
    <text x="233" y="257" font-family="monospace" font-size="8.5" fill="#06b6d4" fill-opacity="0.7" text-anchor="middle" letter-spacing="1.5">FPS GPU</text>

    <text x="350" y="240" font-family="monospace" font-size="21" font-weight="700" fill="#a5b4fc" text-anchor="middle">0.94</text>
    <text x="350" y="257" font-family="monospace" font-size="8.5" fill="#6366f1" fill-opacity="0.7" text-anchor="middle" letter-spacing="1.5">mAP@50</text>

    <text x="467" y="240" font-family="monospace" font-size="21" font-weight="700" fill="#67e8f9" text-anchor="middle">20x</text>
    <text x="467" y="257" font-family="monospace" font-size="8.5" fill="#06b6d4" fill-opacity="0.7" text-anchor="middle" letter-spacing="1.5">FASTER</text>

    <text x="584" y="240" font-family="monospace" font-size="21" font-weight="700" fill="#a5b4fc" text-anchor="middle">90%</text>
    <text x="584" y="257" font-family="monospace" font-size="8.5" fill="#6366f1" fill-opacity="0.7" text-anchor="middle" letter-spacing="1.5">COST SAVED</text>

  </g>
</svg>

<div align="center">

<!-- PREMIUM BANNER -->
<img width="100%" alt="Electric Meter Detection System — AI-powered YOLOv5 pipeline" src="./assets/banner.svg"/>

<br/>

<!-- BADGES ROW 1 -->
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/PyTorch-2.0.1-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/YOLOv5-v7.0.13-00FFFF?style=for-the-badge&logo=github&logoColor=black"/>
<img src="https://img.shields.io/badge/Flask-2.3.3-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-4.8.1-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>

<br/><br/>

<!-- BADGES ROW 2 -->
<img src="https://img.shields.io/badge/Accuracy-95%25+-success?style=flat-square&logo=checkmarx&logoColor=white"/>
<img src="https://img.shields.io/badge/Speed-152%20FPS-blueviolet?style=flat-square&logo=speedtest&logoColor=white"/>
<img src="https://img.shields.io/badge/mAP@50-0.94-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/Model%20Size-14%20MB-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Cost%20Reduction-90%25-green?style=flat-square"/>
<img src="https://img.shields.io/badge/License-MIT-red?style=flat-square"/>

<br/><br/>

<!-- HERO STATS -->
```
╔══════════════════════════════════════════════════════════════╗
║  ⚡  AUTOMATED ELECTRIC METER DETECTION SYSTEM  ⚡           ║
║  ─────────────────────────────────────────────────────────  ║
║   95%+ Precision  │  152 FPS on GPU  │  90% Cost Reduction  ║
║   0.94 mAP@50     │  14 MB Model     │  20× Faster          ║
╚══════════════════════════════════════════════════════════════╝
```

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
│     "processing_ms": 6.5 }                                │
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
│
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
| 📤 Image Upload | Drag & drop or browse image files |
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
⏱  Time/Building   40+ hours    →    2 hours    (95% ↓)
💰  Cost/Inspect  ₹25,000       →   ₹2,000      (90% ↓)
👁  Miss Rate      5–10%        →   < 5%        (2× better)
📊  Accuracy       ~90%         →   95%+        (+5%)
📋  Reports        Manual paper →   Auto JSON   (100% digital)
🔁  Scalability    1 team       →   Unlimited   (fully parallel)
```

> **ROI Positive after just 2 buildings inspected.**

---

## ⚠️ Challenges & Solutions

| Challenge | Solution Applied |
|-----------|-----------------|
| 🔴 CUDA Out-of-Memory (OOM) during training | Reduced batch size from 16 → 8 |
| 🔴 Multiple annotation class IDs from different tools | `fix_labels.py` — normalizes all class IDs to `0` |
| 🔴 Model overfitting on small dataset (1000 images) | Early stopping (patience=20) + SGD + weight decay |
| 🔴 PyTorch import conflicts at startup | Moved `import torch` to top of all entry scripts |
| 🔴 Annotation bottleneck (manual labeling) | Supplemented LabelImg with Roboflow for speed |

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

---

**Built with ❤️ by Sumit Kumar Sahu**

*B.Tech Computer Science (AI & ML) | Internship Project 2026*

*Developed for TPCODL Field Operations Automation*

---


</div>
