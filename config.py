import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:430AMclub!@localhost/wildlife_conservation")

    # YOLOv5 Model Configuration
    YOLO_MODEL_PATH = os.getenv("YOLO_MODEL_PATH", "model/best.pt")  # Correct path to your trained YOLOv5 model
    CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", 0.4))  
    
    # DeepSORT Configuration
    DEEP_SORT_PATH = os.getenv("DEEP_SORT_PATH", "model/deep_sort/deep_sort.py")  # Matches your project's structure

    # Security Configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "your_strong_secret_key_here")
