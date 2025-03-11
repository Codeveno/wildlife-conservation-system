from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from auth.auth_handler import create_user, send_verification_email, generate_verification_code, hash_password, verify_email_code
from database.db_config import get_db_connection

auth_bp = Blueprint('auth', __name__)

# Login Route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = hash_password(request.form['password'])

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Users WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()

        if user:
            if user['verified']:
                session['user'] = user['username']
                return redirect(url_for('dashboard'))
            else:
                return "Account not verified. Please check your email."
        return "Invalid credentials."

    return render_template('login.html')

# Register Route
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        verification_code = generate_verification_code()
        create_user(username, email, password, verification_code)
        send_verification_email(email, verification_code)

        return "Registration successful. Please check your email to verify your account."

    return render_template('register.html')

# Email Verification Route
@auth_bp.route('/verify-email', methods=['POST'])
def verify_email():
    email = request.form['email']
    code = request.form['code']

    if verify_email_code(email, code):
        return "Email verified successfully. You can now log in."
    return "Invalid verification code."

# Password Reset Route
@auth_bp.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']

        new_password = generate_verification_code()  
        hashed_password = hash_password(new_password)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Users SET password = %s WHERE email = %s', (hashed_password, email))
        conn.commit()

        send_verification_email(email, f"Your new password is: {new_password}")
        return "Password reset successful. Check your email for the new password."

    return render_template('reset_password.html')
