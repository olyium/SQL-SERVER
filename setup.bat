@echo off
echo Setting Up
pip install -r requirements.txt
python -m uvicorn server:app --reload