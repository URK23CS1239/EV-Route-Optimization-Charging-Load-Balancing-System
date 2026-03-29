"""
WSGI entry point for Render deployment
This file loads the Flask app from EV_Project/app.py
"""
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app from EV_Project
from EV_Project.app import app

if __name__ == "__main__":
    app.run()
