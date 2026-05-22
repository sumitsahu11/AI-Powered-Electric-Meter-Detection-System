"""Meter detection and inference"""

import torch
import cv2
import numpy as np
import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class MeterDetector:
    """Detect meters in images"""

    def __init__(self, model_path, conf_threshold=0.5):
        try:
            self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
            logger.info(f"Using device: {self.device}")

            self.model = torch.hub.load(
                'ultralytics/yolov5',
                'custom',
                path=str(model_path),
                force_reload=False
            )
            self.model.to(self.device)
            self.conf_threshold = conf_threshold
            logger.info(f"Model loaded: {model_path}")  # removed ✓ to avoid Windows encoding issue
        except Exception as e:
            logger.error(f"Model loading failed: {e}")
            raise

    def detect(self, image):
        """Detect meter in image"""
        try:
            # Run model (AutoShape Detections)
            results = self.model(image)

            # Get detections tensor for first image: shape (N, 6) [x1,y1,x2,y2,conf,cls]
            det = results.xyxy[0]

            # Filter by confidence threshold
            if det is not None and len(det):
                det = det[det[:, 4] >= self.conf_threshold]

            # Convert to numpy array on CPU
            detections = det.cpu().numpy() if det is not None and len(det) else np.empty((0, 6))

            if len(detections) > 0:
                # max confidence
                accuracy = float(detections[:, 4].max())
                detected = True
            else:
                accuracy = 0.0
                detected = False

            # Render annotated image (returns list of images)
            rendered = results.render()[0]  # take first image

            return {
                'detected': detected,
                'accuracy': accuracy,
                'confidence': accuracy,
                'boxes': detections,
                'frame': rendered,
                'detection_count': int(len(detections)),
            }

        except Exception as e:
            logger.error(f"Detection failed: {e}")
            raise

    def process_image(self, image_path, output_dir=None):
        """Process single image"""
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Cannot read: {image_path}")

        results = self.detect(image)

        logger.info(
            f"{Path(image_path).name}: Detected={results['detected']}, "
            f"Accuracy={results['accuracy']:.2%}"
        )

        if output_dir:
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            output_path = os.path.join(output_dir, Path(image_path).stem + '_detected.jpg')
            cv2.imwrite(output_path, results['frame'])

        return results
