import torch
import cv2
import numpy as np
import os
from pathlib import Path

class MeterDetector:
    def __init__(self, model_path):
        """Initialize the YOLOv5 model with YOUR trained best.pt"""
        try:
            self.model = torch.hub.load('ultralytics/yolov5', 'custom', 
                                       path=model_path, force_reload=False)
            self.model.conf = 0.45  # Confidence threshold
            self.model.iou = 0.45   # IOU threshold
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None
    
    def detect(self, image_path):
        """Detect meters in image using YOUR trained model"""
        if self.model is None:
            return {
                'detected': False,
                'accuracy': 0,
                'confidence': 0,
                'boxes': [],
                'image_annotated': None
            }
        
        # Read image
        img = cv2.imread(image_path)
        if img is None:
            return {'detected': False, 'accuracy': 0, 'confidence': 0}
        
        # Run inference with YOUR model
        results = self.model(img)
        
        # Parse results
        # Parse results using pandas()
        df = results.pandas().xyxy[0]   # DataFrame with one row per detection
        detections = df.values          # Convert to numpy array

        detected = len(detections) > 0
        accuracy = float(detections[0][4]) if detected else 0  # 5th column = confidence
        
        detected = len(detections) > 0
        accuracy = float(detections[0, 4]) if detected else 0
        
        # Draw boxes on image
        annotated = self._draw_boxes(img.copy(), detections)
        
        return {
            'detected': detected,
            'accuracy': accuracy,
            'confidence': accuracy,
            'boxes': detections.tolist() if detected else [],
            'image_annotated': annotated
        }
    
    def _draw_boxes(self, image, detections):
        """Draw bounding boxes on image"""
        for det in detections:
            x1, y1, x2, y2, conf, cls = det[:6]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
            
            # Draw rectangle
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Add confidence label
            label = f'Meter {conf:.2f}'
            cv2.putText(image, label, (x1, y1-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return image
