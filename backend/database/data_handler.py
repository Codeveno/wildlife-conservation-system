from .db_config import get_db_connection, SessionLocal
from .models import User, VerificationCode
from sqlalchemy.exc import IntegrityError
import bcrypt
import random

# ======================== USER MANAGEMENT FUNCTIONS ======================== #

# Hashing the password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Verify hashed password
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Create new user
def create_user(username, email, password):
    db = SessionLocal()
    hashed_password = hash_password(password)
    new_user = User(username=username, email=email, password=hashed_password)
    
    try:
        db.add(new_user)
        db.commit()
        return True, "Account created successfully. Please check your email for verification."
    except IntegrityError:
        db.rollback()
        return False, "Username or email already exists."
    finally:
        db.close()

# Store verification code
def store_verification_code(email):
    db = SessionLocal()
    code = str(random.randint(100000, 999999))
    verification_entry = VerificationCode(email=email, code=code)
    
    db.add(verification_entry)
    db.commit()
    db.close()

    return code

# Verify the user's email
def verify_user_email(email, code):
    db = SessionLocal()
    verification_entry = db.query(VerificationCode).filter_by(email=email, code=code).first()

    if verification_entry:
        user = db.query(User).filter_by(email=email).first()
        if user:
            user.is_verified = True
            db.commit()
            db.close()
            return True, "Account verified successfully."
    
    db.close()
    return False, "Invalid verification code."

# ====================== ANIMAL TRACKING FUNCTIONS ====================== #

# Insert animal tracking data
def insert_animal_tracking(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO AnimalTracking (animal_name, location)
        VALUES (%s, %s)
    ''', (data['animal_name'], data['location']))

    conn.commit()
    conn.close()

# Retrieve all animal tracking records
def get_all_records():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM AnimalTracking')
    results = cursor.fetchall()
    conn.close()
    return results
