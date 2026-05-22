import torch
print("torch test in run_step_4:", torch.__version__, torch.randn(1))

from src.config import Config


from src.config import Config
config = Config()

import torch
print("torch in run_step_4:", torch.__version__)  # temporary debug

from src.config import Config
from src.pipeline import MeterDetectionPipeline  # if used here
# ...rest of imports...

#!/usr/bin/env python3
"""Step 4: Train YOLOv5s model"""

import os
import sys
import subprocess
from src.config import Config


if __name__ == "__main__":
    try:
        config = Config()
        dataset_yaml = config.DATASET_DIR / "dataset.yaml"

        if not dataset_yaml.exists():
            print("❌ Dataset not found. Run: python run_step_3.py")
            sys.exit(1)

        print("\n" + "=" * 60)
        print("STEP 4: TRAINING MODEL")
        print("=" * 60)

        # Build command using the current Python interpreter (venv)
        cmd = (
            f'"{sys.executable}" yolov5/train.py '
            f'--img {config.IMG_SIZE} '
            f'--batch {config.BATCH_SIZE} '
            f'--epochs {config.EPOCHS} '
            f'--data "{dataset_yaml}" '
            f'--weights {config.PRETRAINED_WEIGHTS} '
            f'--device {config.DEVICE} '
            f'--patience {config.PATIENCE} '
            f'--project models '
            f'--name meter_detection '
            f'--exist-ok '
            f'--workers {config.WORKERS}'
)


        print(f"\nRunning: {cmd}\n")

        # Run training and check for errors
        result = subprocess.run(cmd, shell=True)

        if result.returncode != 0:
            print("\n❌ Training failed (see error above)")
            sys.exit(result.returncode)

        print("\n✅ Training complete!")
        print("👉 Next: Run inference with: python run_step_5.py")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
