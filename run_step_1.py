#!/usr/bin/env python3
"""Step 1: Extract frames from video"""

import sys
import logging
from src.pipeline import MeterDetectionPipeline

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        pipeline = MeterDetectionPipeline()
        num_frames = pipeline.step1_extract_frames()
        print(f"\n✅ Success! Extracted {num_frames} frames")
        print("👉 Next: Annotate frames using Roboflow or LabelImg")
        print("   Save annotations to: data/frames/annotated/")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
