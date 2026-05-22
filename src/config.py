"""Configuration management"""

import os
from pathlib import Path

class Config:
    """Project configuration"""
    
    # Paths
    PROJECT_ROOT = Path(__file__).parent.parent
    DATA_DIR = PROJECT_ROOT / 'data'
    VIDEO_DIR = DATA_DIR / 'videos'
    FRAMES_EXTRACTED = DATA_DIR / 'frames' / 'extracted'
    FRAMES_ANNOTATED = DATA_DIR / 'frames' / 'annotated'
    DATASET_DIR = DATA_DIR / 'dataset'
    MODELS_DIR = PROJECT_ROOT / 'models'
    RESULTS_DIR = PROJECT_ROOT / 'results'
    LOGS_DIR = RESULTS_DIR / 'logs'
    
    # Create directories
    for dir_path in [DATA_DIR, VIDEO_DIR, FRAMES_EXTRACTED, FRAMES_ANNOTATED, 
                     DATASET_DIR, MODELS_DIR, RESULTS_DIR, LOGS_DIR]:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Video settings
    FRAME_INTERVAL = 5  # Extract every Nth frame
    VIDEO_PATH = VIDEO_DIR / 'sample_meter_video.mp4'
    
    # Dataset settings
    TRAIN_RATIO = 0.7
    VAL_RATIO = 0.15
    TEST_RATIO = 0.15
    
    # Training settings
    IMG_SIZE = 640
    BATCH_SIZE = 16
    EPOCHS = 25
    PATIENCE = 20
    DEVICE = "cpu"  # GPU device ID, or 'cpu'
    WORKERS = 0  
    
    # Model settings
    MODEL_PATH = MODELS_DIR / 'meter_detection' / 'weights' / 'best.pt'
    PRETRAINED_WEIGHTS = 'yolov5s.pt'
    
    # Inference settings
    CONF_THRESHOLD = 0.5
    IOU_THRESHOLD = 0.45
    
    # Database settings (optional)
    DB_USERNAME = os.getenv('DB_USERNAME', 'your_username')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'your_password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 1521))
    DB_SERVICE = os.getenv('DB_SERVICE', 'ORCL')
    
    @classmethod
    def to_dict(cls):
        """Convert config to dictionary"""
        return {
            'frame_interval': cls.FRAME_INTERVAL,
            'img_size': cls.IMG_SIZE,
            'batch_size': cls.BATCH_SIZE,
            'epochs': cls.EPOCHS,
            'device': cls.DEVICE,
            'workers': cls.WORKERS,  # added
        }
