"""Dataset preparation for YOLO training"""

import os
import shutil
from pathlib import Path
import logging
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)

class DatasetPreparer:
    """Prepare dataset in YOLO format"""
    
    def __init__(self, images_dir, labels_dir, output_dir, train_ratio=0.7, val_ratio=0.15):
        self.images_dir = images_dir
        self.labels_dir = labels_dir
        self.output_dir = output_dir
        self.train_ratio = train_ratio
        self.val_ratio = val_ratio
        self.test_ratio = 1 - train_ratio - val_ratio
        
        self._create_structure()
        logger.info(f"DatasetPreparer initialized")
    
    def _create_structure(self):
        """Create directory structure"""
        for split in ['train', 'val', 'test']:
            Path(self.output_dir, 'images', split).mkdir(parents=True, exist_ok=True)
            Path(self.output_dir, 'labels', split).mkdir(parents=True, exist_ok=True)
    
    def prepare(self):
        """Prepare dataset"""
        try:
            images = [f for f in os.listdir(self.images_dir)
                     if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            
            logger.info(f"Found {len(images)} images")
            
            # Split dataset
            train_imgs, temp_imgs = train_test_split(
                images,
                test_size=(1 - self.train_ratio),
                random_state=42
            )
            
            val_imgs, test_imgs = train_test_split(
                temp_imgs,
                test_size=self.test_ratio / (1 - self.train_ratio),
                random_state=42
            )
            
            logger.info(f"Split: train={len(train_imgs)}, val={len(val_imgs)}, test={len(test_imgs)}")
            
            # Copy files
            for split, files in [('train', train_imgs), ('val', val_imgs), ('test', test_imgs)]:
                for img in files:
                    src_img = os.path.join(self.images_dir, img)
                    dst_img = os.path.join(self.output_dir, 'images', split, img)
                    shutil.copy2(src_img, dst_img)
                    
                    src_label = os.path.join(self.labels_dir, Path(img).stem + '.txt')
                    if os.path.exists(src_label):
                        dst_label = os.path.join(self.output_dir, 'labels', split, Path(img).stem + '.txt')
                        shutil.copy2(src_label, dst_label)
            
            # Create dataset.yaml
            self._create_yaml()
            
            logger.info("Dataset preparation complete")
            
            return {
                'train': len(train_imgs),
                'val': len(val_imgs),
                'test': len(test_imgs)
            }
            
        except Exception as e:
            logger.error(f"Preparation failed: {e}")
            raise
    
    def _create_yaml(self):
        """Create dataset.yaml"""
        content = f"""path: {os.path.abspath(self.output_dir)}
train: images/train
val: images/val
test: images/test
nc: 1
names: ['meter']
"""
        
        yaml_path = os.path.join(self.output_dir, 'dataset.yaml')
        with open(yaml_path, 'w') as f:
            f.write(content)
        
        logger.info("Created dataset.yaml")
