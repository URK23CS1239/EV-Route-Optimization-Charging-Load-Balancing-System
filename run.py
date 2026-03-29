#!/usr/bin/env python
"""
Run the EV Project Flask Application
This script must be run from the project root directory
"""

import os
import sys
from EV_Project.app import app

if __name__ == '__main__':
    # Ensure we're in the right directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 50)
    print("⚡ EV Route Planner Starting...")
    print("=" * 50)
    print("Opening: http://localhost:5000")
    print("Press CTRL+C to stop the server")
    print("=" * 50)
    
    app.run(debug=True, host='localhost', port=5000)
