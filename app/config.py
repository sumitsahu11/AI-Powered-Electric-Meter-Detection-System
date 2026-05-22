import os

class Config:
    # Detection Settings
    GOOD_ACCURACY_THRESHOLD = 0.2  # 20% accuracy = good detection
    BAD_ACCURACY_THRESHOLD = 0.0   # Below this = bad detection
    
    # File Settings
    UPLOAD_FOLDER = os.path.join('app', 'uploads', 'input')
    GOOD_FOLDER = os.path.join('app', 'uploads', 'good_detections')
    BAD_FOLDER = os.path.join('app', 'uploads', 'bad_detections')
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'bmp'}
    
    # Model Settings - USES YOUR TRAINED MODEL!
    MODEL_PATH = 'models/meter_detection/weights/best.pt'
    
    # App Settings
    SECRET_KEY = 'your-secret-key-change-this'
    DEBUG = False
