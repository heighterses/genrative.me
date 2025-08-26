#!/bin/bash

# Quick Start Script for genrative.me DataFlow Academy Application
# This script automates the setup and running process

echo "🚀 Starting DataFlow Academy Application Setup..."
echo ""

# Navigate to project directory
echo "📁 Navigating to project directory..."
cd /Users/user/Desktop/genrative.me

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Check if requirements are installed
echo "📦 Installing/checking dependencies..."
pip install -r requirements.txt

echo ""
echo "🎉 Setup complete! Starting Flask application..."
echo ""
echo "📱 Your DataFlow Academy app will be available at:"
echo "   http://localhost:8000"
echo ""
echo "⏹️  To stop the server, press Ctrl+C"
echo ""

# Start the Flask application
python app.py
