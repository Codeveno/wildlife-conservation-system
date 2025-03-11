from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql  

# Database URL for MySQL
DATABASE_URL = "mysql+pymysql://root:430AMclub!@localhost/wildlife_conservation"

# Engine configuration
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Session configuration
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model for inheritance
Base = declarative_base()

# Corrected init_db function
def init_db():
    try:
        from backend.database import models  
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully.")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
    finally:
        engine.dispose()  
