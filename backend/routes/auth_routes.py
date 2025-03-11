import os
from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for
from backend.database.models import SessionLocal, User
from werkzeug.security import generate_password_hash, check_password_hash
import random
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv  # Add this import

# Load environment variables
load_dotenv()

auth_bp = Blueprint('auth', __name__)

# Email Configuration
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Send Verification Email
def send_verification_email(email, code):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Email Verification Code'
        msg['From'] = EMAIL_USER
        msg['To'] = email
        msg.set_content(f'Your verification code is: {code}')

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
    except Exception as e:
        print(f"Email sending failed: {e}")
