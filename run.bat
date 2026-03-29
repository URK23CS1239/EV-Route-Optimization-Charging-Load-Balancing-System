@echo off
REM Run EV Project Flask App
REM This script must be run from the project root directory

cd /d "%~dp0"
python -m flask --app EV_Project/app.py run
