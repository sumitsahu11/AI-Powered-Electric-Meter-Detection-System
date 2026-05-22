<div align="center">

<!-- PREMIUM BANNER -->
<svg width="100%" viewBox="0 0 860 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0a0a14"/>
      <stop offset="50%" style="stop-color:#0f0c29"/>
      <stop offset="100%" style="stop-color:#0d1117"/>
    </linearGradient>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#e0e7ff"/>
      <stop offset="40%" style="stop-color:#a5b4fc"/>
      <stop offset="100%" style="stop-color:#06b6d4"/>
    </linearGradient>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:transparent"/>
      <stop offset="30%" style="stop-color:#6366f1;stop-opacity:0.7"/>
      <stop offset="70%" style="stop-color:#06b6d4;stop-opacity:0.7"/>
      <stop offset="100%" style="stop-color:transparent"/>
    </linearGradient>
    <linearGradient id="statGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#a5b4fc;stop-opacity:0.08"/>
      <stop offset="100%" style="stop-color:#06b6d4;stop-opacity:0.04"/>
    </linearGradient>
    <filter id="glow1">
      <feGaussianBlur stdDeviation="40" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <clipPath id="clip"><rect width="860" height="300" rx="14"/></clipPath>
  </defs>

  <!-- Background -->
  <rect width="860" height="300" rx="14" fill="url(#bg)"/>
  <g clip-path="url(#clip)">

    <!-- Grid lines -->
    <g stroke="rgba(99,102,241,0.07)" stroke-width="0.5">
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
    <ellipse cx="120" cy="80" rx="200" ry="160" fill="#6366f1" opacity="0.06" filter="url(#glow1)"/>
    <ellipse cx="780" cy="240" rx="160" ry="120" fill="#06b6d4" opacity="0.07" filter="url(#glow1)"/>
    <ellipse cx="500" cy="150" rx="120" ry="100" fill="#a78bfa" opacity="0.04" filter="url(#glow1)"/>

    <!-- Detection box decorations (right side) -->
    <rect x="700" y="44" width="56" height="42" rx="2" fill="none" stroke="#06b6d4" stroke-width="1.2" opacity="0.5"/>
    <text x="703" y="40" font-family="monospace" font-size="8" fill="#06b6d4" opacity="0.7">meter 0.96</text>
    <rect x="734" y="106" width="46" height="34" rx="2" fill="none" stroke="#06b6d4" stroke-width="1.2" opacity="0.38"/>
    <text x="737" y="102" font-family="monospace" font-size="8" fill="#06b6d4" opacity="0.55">meter 0.91</text>
    <rect x="700" y="174" width="60" height="44" rx="2" fill="none" stroke="#a5b4fc" stroke-width="1.2" opacity="0.35"/>
    <text x="703" y="170" font-family="monospace" font-size="8" fill="#a5b4fc" opacity="0.5">meter 0.94</text>

    <!-- Dots scatter -->
    <circle cx="680" cy="60" r="2" fill="#6366f1" opacity="0.5"/>
    <circle cx="800" cy="90" r="1.5" fill="#06b6d4" opacity="0.4"/>
    <circle cx="760" cy="160" r="2.5" fill="#a78bfa" opacity="0.3"/>
    <circle cx="820" cy="200" r="1.5" fill="#6366f1" opacity="0.4"/>
    <circle cx="660" cy="230" r="2" fill="#06b6d4" opacity="0.3"/>
    <circle cx="80" cy="240" r="1.5" fill="#6366f1" opacity="0.3"/>
    <circle cx="40" cy="180" r="2" fill="#06b6d4" opacity="0.25"/>

    <!-- Corner brackets -->
    <path d="M18 28 L18 14 L32 14" fill="none" stroke="#6366f1" stroke-width="1.8" stroke-linecap="round" opacity="0.8"/>
    <path d="M842 28 L842 14 L828 14" fill="none" stroke="#06b6d4" stroke-width="1.8" stroke-linecap="round" opacity="0.8"/>
    <path d="M18 272 L18 286 L32 286" fill="none" stroke="#06b6d4" stroke-width="1.8" stroke-linecap="round" opacity="0.8"/>
    <path d="M842 272 L842 286 L828 286" fill="none" stroke="#6366f1" stroke-width="1.8" stroke-linecap="round" opacity="0.8"/>

    <!-- Eyebrow -->
    <text x="430" y="52" font-family="monospace" font-size="10" fill="#6366f1" opacity="0.85" text-anchor="middle" letter-spacing="4">INTERNSHIP PROJECT · TPCODL · 2026</text>
    <rect x="200" y="57" width="460" height="0.6" fill="url(#lineGrad)"/>

    <!-- Main Title -->
    <text x="390" y="118" font-family="'Segoe UI', Arial Black, sans-serif" font-size="46" font-weight="700" fill="url(#titleGrad)" text-anchor="middle" letter-spacing="-1.5">Electric Meter</text>
    <text x="390" y="168" font-family="'Segoe UI', Arial Black, sans-serif" font-size="46" font-weight="700" fill="url(#titleGrad)" text-anchor="middle" letter-spacing="-1.5">Detection System</text>

    <!-- Subtitle -->
    <text x="390" y="192" font-family="monospace" font-size="11" fill="#a5b4fc" opacity="0.65" text-anchor="middle" letter-spacing="1">automated ai pipeline · yolov5 + pytorch · flask rest api</text>

    <!-- Stats bar -->
    <rect x="60" y="210" width="582" height="62" rx="8" fill="url(#statGrad)" stroke="rgba(99,102,241,0.2)" stroke-width="0.8"/>

    <!-- Dividers -->
    <line x1="176" y1="222" x2="176" y2="260" stroke="rgba(99,102,241,0.2)" stroke-width="0.8"/>
    <line x1="292" y1="222" x2="292" y2="260" stroke="rgba(99,102,241,0.2)" stroke-width="0.8"/>
    <line x1="408" y1="222" x2="408" y2="260" stroke="rgba(99,102,241,0.2)" stroke-width="0.8"/>
    <line x1="524" y1="222" x2="524" y2="260" stroke="rgba(99,102,241,0.2)" stroke-width="0.8"/>

    <!-- Stat 1 -->
    <text x="118" y="240" font-family="monospace" font-size="20" font-weight="700" fill="#a5b4fc" text-anchor="middle">95%+</text>
    <text x="118" y="257" font-family="monospace" font-size="9" fill="#6366f1" opacity="0.7" text-anchor="middle" letter-spacing="1.5">PRECISION</text>

    <!-- Stat 2 -->
    <text x="234" y="240" font-family="monospace" font-size="20" font-weight="700" fill="#67e8f9" text-anchor="middle">152</text>
    <text x="234" y="257" font-family="monospace" font-size="9" fill="#06b6d4" opacity="0.7" text-anchor="middle" letter-spacing="1.5">FPS (GPU)</text>

    <!-- Stat 3 -->
    <text x="350" y="240" font-family="monospace" font-size="20" font-weight="700" fill="#a5b4fc" text-anchor="middle">0.94</text>
    <text x="350" y="257" font-family="monospace" font-size="9" fill="#6366f1" opacity="0.7" text-anchor="middle" letter-spacing="1.5">mAP@50</text>

    <!-- Stat 4 -->
    <text x="466" y="240" font-family="monospace" font-size="20" font-weight="700" fill="#67e8f9" text-anchor="middle">20×</text>
    <text x="466" y="257" font-family="monospace" font-size="9" fill="#06b6d4" opacity="0.7" text-anchor="middle" letter-spacing="1.5">FASTER</text>

    <!-- Stat 5 -->
    <text x="582" y="240" font-family="monospace" font-size="20" font-weight="700" fill="#a5b4fc" text-anchor="middle">90%</text>
    <text x="582" y="257" font-family="monospace" font-size="9" fill="#6366f1" opacity="0.7" text-anchor="middle" letter-spacing="1.5">COST SAVED</text>

  </g>
</svg>

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

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,100:302b63&height=100&section=footer"/>

</div>
