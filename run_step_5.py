import torch
print("torch test in run_step_5:", torch.__version__, torch.randn(1))

from src.pipeline import MeterDetectionPipeline

#!/usr/bin/env python3
"""Step 5: Run inference on test set"""

import sys
import logging
from src.pipeline import MeterDetectionPipeline

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        pipeline = MeterDetectionPipeline()
        pipeline.step5_run_inference()
        print("\n✅ Inference complete!")
        print("📊 Results saved to: results/detections/")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
