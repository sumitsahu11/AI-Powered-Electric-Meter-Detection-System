"""Main pipeline orchestration"""

import os
import logging
from pathlib import Path
from .config import Config
from .frame_extractor import FrameExtractor
from .dataset_preparer import DatasetPreparer
from .meter_detector import MeterDetector

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Path(__file__).parent.parent / 'results' / 'logs' / 'pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MeterDetectionPipeline:
    """Complete meter detection pipeline"""
    
    def __init__(self):
        self.config = Config()
        logger.info("Pipeline initialized")
    
    def step1_extract_frames(self):
        """Step 1: Extract frames from video"""
        logger.info("\n" + "="*60)
        logger.info("STEP 1: EXTRACTING FRAMES")
        logger.info("="*60)
        
        extractor = FrameExtractor(
            video_path=str(self.config.VIDEO_PATH),
            output_dir=str(self.config.FRAMES_EXTRACTED),
            frame_interval=self.config.FRAME_INTERVAL
        )
        return extractor.extract()
    
    def step3_prepare_dataset(self):
        """Step 3: Prepare dataset"""
        logger.info("\n" + "="*60)
        logger.info("STEP 3: PREPARING DATASET")
        logger.info("="*60)
        
        preparer = DatasetPreparer(
            images_dir=str(self.config.FRAMES_EXTRACTED),
            labels_dir=str(self.config.FRAMES_ANNOTATED),
            output_dir=str(self.config.DATASET_DIR),
            train_ratio=self.config.TRAIN_RATIO,
            val_ratio=self.config.VAL_RATIO
        )
        return preparer.prepare()
    
    def step5_run_inference(self):
        """Step 5: Run inference"""
        logger.info("\n" + "="*60)
        logger.info("STEP 5: RUNNING INFERENCE")
        logger.info("="*60)
        
        if not self.config.MODEL_PATH.exists():
            logger.warning(f"Model not found: {self.config.MODEL_PATH}")
            return None
        
        detector = MeterDetector(
            model_path=str(self.config.MODEL_PATH),
            conf_threshold=self.config.CONF_THRESHOLD
        )
        
        test_dir = self.config.DATASET_DIR / 'images' / 'test'
        output_dir = self.config.RESULTS_DIR / 'detections'
        
        if not test_dir.exists():
            logger.warning(f"Test directory not found: {test_dir}")
            return None
        
        total_accuracy = 0
        images_count = 0
        detected_count = 0
        
        for img_file in os.listdir(test_dir):
            if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(test_dir, img_file)
                result = detector.process_image(img_path, output_dir)
                
                total_accuracy += result['accuracy']
                images_count += 1
                if result['detected']:
                    detected_count += 1
        
        if images_count > 0:
            avg_accuracy = total_accuracy / images_count
            logger.info(f"\nResults: {detected_count}/{images_count} detected, "
                       f"Accuracy: {avg_accuracy:.2%}")
