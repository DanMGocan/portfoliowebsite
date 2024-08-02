from app import app
from flask import render_template

# Importing the views
from app.views.google_vision import google_vision_bp

# Register the blueprints
app.register_blueprint(google_vision_bp)

@app.route('/')
def index():
    return render_template('index.html')

