"""Frame extraction from video"""

import cv2
import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class FrameExtractor:
    """Extract frames from video file"""
    
    def __init__(self, video_path, output_dir, frame_interval=5):
        self.video_path = video_path
        self.output_dir = output_dir
        self.frame_interval = frame_interval
        
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        logger.info(f"FrameExtractor initialized: {video_path}")
    
    def extract(self):
        """Extract frames"""
        try:
            cap = cv2.VideoCapture(str(self.video_path))
            
            if not cap.isOpened():
                raise ValueError(f"Cannot open video: {self.video_path}")
            
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            logger.info(f"Video: {total_frames} frames @ {fps} FPS")
            
            frame_count = 0
            saved_count = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                if frame_count % self.frame_interval == 0:
                    filename = os.path.join(self.output_dir, f"frame_{saved_count:06d}.jpg")
                    cv2.imwrite(filename, frame)
                    saved_count += 1
                    
                    if saved_count % 50 == 0:
                        logger.info(f"Extracted {saved_count} frames...")
                
                frame_count += 1
            
            cap.release()
            logger.info(f"✓ Extraction complete: {saved_count} frames")
            return saved_count
            
        except Exception as e:
            logger.error(f"Extraction failed: {e}")
            raise
