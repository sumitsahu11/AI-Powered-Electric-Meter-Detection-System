<div align="center">

<img src="banner.svg" alt="Electric Meter Detection System" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![YOLOv5](https://img.shields.io/badge/YOLOv5-00FFFF?style=for-the-badge&logo=github&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

<br/>

> **Internship Project @ TPCODL · 2026**
> An automated AI pipeline to detect and localize electric meters in field images using YOLOv5 + PyTorch, served via a Flask REST API.

</div>

---

## Table of Contents

- [Overview](#overview)
- [Key Metrics](#key-metrics)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Model Details](#model-details)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **Electric Meter Detection System** is a deep learning-based computer vision pipeline developed during an internship at **TPCODL (TP Central Odisha Distribution Limited)**. It automates the detection and localization of electric meters in field-captured images, replacing manual inspection workflows with a fast, accurate AI solution.

The system uses a fine-tuned **YOLOv5** model trained on a custom dataset of electric meter images, wrapped in a **Flask REST API** for easy integration into existing infrastructure.

---

## Key Metrics

<div align="center">

| Metric | Value |
|--------|-------|
| Precision | **95%+** |
| Recall | **96%** |
| mAP@50 | **0.94** |
| GPU Inference Speed | **152 FPS** |
| Speed vs Manual | **20× Faster** |
| Cost Reduction | **90%** |
| Model Size | **14 MB** |
| Training Images | **1,000** |

</div>

---

## Features

- **Real-time Detection** — 152 FPS on GPU, 6.5 ms per image
- **High Accuracy** — 95%+ precision, 96% recall on test set
- **Lightweight Model** — Only 14 MB, deployable on edge devices
- **REST API** — Flask-based API for easy integration
- **Batch Processing** — Process multiple images in a single request
- **Logging & Storage** — Detection results stored in SQLite database
- **OpenCV Integration** — Pre/post-processing pipeline with OpenCV
- **Custom Trained** — Fine-tuned YOLOv5 on 1,000 labeled meter images

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Model | YOLOv5 (custom fine-tuned) |
| Framework | PyTorch 2.x |
| API Server | Flask REST API |
| Image Processing | OpenCV |
| Database | SQLite |
| Language | Python 3.10+ |
| Training | Google Colab / Local GPU |

---

## Project Structure

```
electric-meter-detection/
│
├── model/
│   ├── best.pt                  # Trained YOLOv5 weights
│   └── yolov5s.yaml             # Model config
│
├── api/
│   ├── app.py                   # Flask REST API
│   ├── detect.py                # Detection logic
│   └── utils.py                 # Helper functions
│
├── data/
│   ├── images/                  # Training & test images
│   ├── labels/                  # YOLO format annotations
│   └── dataset.yaml             # Dataset config
│
├── notebooks/
│   └── train_yolov5.ipynb       # Training notebook
│
├── results/
│   └── detection_samples/       # Sample output images
│
├── requirements.txt
├── banner.svg
└── README.md
```

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/electric-meter-detection.git
cd electric-meter-detection
```

**2. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Download YOLOv5**

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

---

## Usage

### Run Detection on a Single Image

```python
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best.pt')
results = model('path/to/meter_image.jpg')
results.show()
results.save('results/')
```

### Start the Flask API Server

```bash
python api/app.py
```

Server starts at `http://localhost:5000`

### Send a Detection Request

```bash
curl -X POST http://localhost:5000/detect \
  -F "image=@meter.jpg" \
  -H "Content-Type: multipart/form-data"
```

---

## API Reference

### `POST /detect`

Detect electric meters in an uploaded image.

**Request**
```
Content-Type: multipart/form-data
Body: image (file)
```

**Response**
```json
{
  "status": "success",
  "detections": [
    {
      "label": "meter",
      "confidence": 0.96,
      "bbox": [x1, y1, x2, y2]
    }
  ],
  "inference_time_ms": 6.5,
  "image_id": "abc123"
}
```

### `GET /health`

Check if the API server is running.

**Response**
```json
{ "status": "ok", "model": "loaded" }
```

### `GET /results/<image_id>`

Retrieve past detection results from the database.

---

## Model Details

| Parameter | Value |
|-----------|-------|
| Base Model | YOLOv5s |
| Input Size | 640 × 640 |
| Classes | 1 (electric meter) |
| Epochs | 100 |
| Batch Size | 16 |
| Optimizer | SGD |
| Training Images | 800 |
| Validation Images | 200 |
| Augmentation | Mosaic, Flip, HSV |

---

## Results

<div align="center">

```
Precision:  ████████████████████  95.2%
Recall:     █████████████████████ 96.1%
mAP@0.5:    ████████████████████  94.0%
mAP@0.5:95: ███████████████       72.3%
```

</div>

Sample detections show bounding boxes with confidence scores drawn around each detected meter in field-captured images across varied lighting and orientation conditions.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ during Internship at **TPCODL · 2026**

</div>
