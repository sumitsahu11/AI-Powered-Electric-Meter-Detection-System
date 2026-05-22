#!/usr/bin/env python3
"""Run complete pipeline (interactive)"""

import sys
import os
import logging
from src.pipeline import MeterDetectionPipeline
from src.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    print("\n" + "="*70)
    print("METER DETECTION PROJECT - FULL PIPELINE")
    print("="*70)
    
    config = Config()
    pipeline = MeterDetectionPipeline()
    
    print("\n📋 CHECKING PREREQUISITES...\n")
    
    if not config.VIDEO_PATH.exists():
        print(f"⚠️  Video not found: {config.VIDEO_PATH}")
        print("   Place your meter video at: data/videos/sample_meter_video.mp4")
        return
    
    print("\n📍 STEP 1: EXTRACTING FRAMES")
    try:
        num_frames = pipeline.step1_extract_frames()
        print(f"✅ Extracted {num_frames} frames\n")
    except Exception as e:
        print(f"❌ Frame extraction failed: {e}")
        return
    
    print("\n📍 STEP 2: MANUAL ANNOTATION REQUIRED")
    print("Please annotate frames using:")
    print("  -  Roboflow: https://roboflow.com (recommended)")
    print("  -  LabelImg: pip install labelImg && labelImg")
    print("  -  CVAT: https://www.cvat.ai/")
    print("\nSave labels to: data/frames/annotated/")
    
    input("\n⏸️  Press ENTER when annotation is complete...")
    
    annotated_files = list(config.FRAMES_ANNOTATED.glob("*.txt"))
    if len(annotated_files) == 0:
        print("❌ No annotation files found!")
        return
    
    print(f"✅ Found {len(annotated_files)} annotation files\n")
    
    print("📍 STEP 3: PREPARING DATASET")
    try:
        splits = pipeline.step3_prepare_dataset()
        print(f"✅ Dataset ready: train={splits['train']}, "
              f"val={splits['val']}, test={splits['test']}\n")
    except Exception as e:
        print(f"❌ Dataset preparation failed: {e}")
        return
    
    print("📍 STEP 4: TRAINING MODEL")
    print("Starting training... (30-120 minutes)\n")
    
    try:
        os.system("python run_step_4.py")
    except Exception as e:
        print(f"❌ Training failed: {e}")
        return
    
    print("\n📍 STEP 5: RUNNING INFERENCE")
    try:
        pipeline.step5_run_inference()
        print("✅ Inference complete!\n")
    except Exception as e:
        print(f"❌ Inference failed: {e}")
        return
    
    print("="*70)
    print("✅ PIPELINE COMPLETE!")
    print("="*70)
    print(f"\n📊 Results saved to: {config.RESULTS_DIR}/detections/")
    print(f"📈 Model saved to: {config.MODELS_DIR}/meter_detection/weights/best.pt")
    print(f"📋 Logs saved to: {config.LOGS_DIR}/")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Pipeline interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
