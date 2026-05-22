import torch  # add this as the first import
print("torch in run_step_3:", torch.__version__)  # temporary debug line

from src.pipeline import MeterDetectionPipeline
# ...rest of your imports and code...

#!/usr/bin/env python3
"""Step 3: Prepare dataset for training"""

import sys
import logging
from src.pipeline import MeterDetectionPipeline

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        pipeline = MeterDetectionPipeline()
        splits = pipeline.step3_prepare_dataset()
        print(f"\n✅ Dataset ready!")
        print(f"   Train: {splits['train']} images")
        print(f"   Val:   {splits['val']} images")
        print(f"   Test:  {splits['test']} images")
        print("👉 Next: Run training")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
