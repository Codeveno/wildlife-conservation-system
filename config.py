import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql://user:430AMclub!@localhost/database")

    # YOLOv5 Model Configuration
    YOLO_MODEL_PATH = os.getenv("YOLO_MODEL_PATH", "model/best.pt")
    CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", 0.4))  
    
    # DeepSORT Configuration
    DEEP_SORT_PATH = os.getenv("DEEP_SORT_PATH", "model/deep_sort.pt")

    # Security Configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key_for_dev")

