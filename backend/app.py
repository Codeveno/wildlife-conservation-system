from flask import Flask, redirect, url_for
from backend.routes.detection_routes import detection_bp
from backend.routes.tracking_routes import tracking_bp
from backend.routes.insights_routes import insights_bp
from backend.auth.auth_routes import auth_bp
from backend.database.models import create_tables

app = Flask(__name__)
app.secret_key = 'wildlife_system_secret_key'

# Register blueprints
app.register_blueprint(detection_bp)
app.register_blueprint(tracking_bp)
app.register_blueprint(insights_bp)
app.register_blueprint(auth_bp)

# Create tables before running
with app.app_context():
    create_tables()

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
