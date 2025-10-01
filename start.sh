#!/bin/bash

# Render deployment startup script
echo "Starting Ri Portfolio deployment..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Start the application with Gunicorn
echo "Starting application with Gunicorn..."
exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 120 app:app