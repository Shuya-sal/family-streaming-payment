#!/bin/bash

# ==========================================
# AUTOMATIC SETUP SCRIPT
# Family Streaming Payment System
# ==========================================

echo "🚀 Starting Setup for Family Streaming Payment System..."
echo ""

# Step 1: Check Python version
echo "Step 1: Checking Python version..."
if command -v python3 &> /dev/null; then
    python3 --version
    echo "✅ Python found!"
else
    echo "❌ Python not installed. Please install Python 3.8+"
    exit 1
fi
echo ""

# Step 2: Create virtual environment
echo "Step 2: Creating virtual environment..."
cd /home/ubuntu/workspace
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created!"
else
    echo "ℹ️  Virtual environment already exists"
fi
echo ""

# Step 3: Activate virtual environment
echo "Step 3: Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated!"
echo ""

# Step 4: Install dependencies
echo "Step 4: Installing dependencies..."
pip install -r requirements.txt
echo "✅ Dependencies installed!"
echo ""

# Step 5: Initialize database
echo "Step 5: Initializing database..."
export FLASK_APP=app.py
python app.py &
sleep 2
curl http://localhost:5000 > /dev/null && echo "✅ Database initialized and server started!" || echo "⚠️  Server may have issues"
pkill -f "python app.py" || true
echo ""

# Step 6: Setup Git (optional)
read -p "Step 6: Do you want to setup Git repository? (y/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial family streaming payment system setup"
    echo "✅ Git repository initialized!"
    
    read -p "Do you want to push to GitHub? (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter your GitHub repository URL: " repo_url
        git remote add origin "$repo_url"
        git branch -M main
        git push -u origin main
        echo "✅ Pushed to GitHub!"
    fi
fi
echo ""

# Step 7: Show summary
echo "========================================="
echo "✅ SETUP COMPLETED SUCCESSFULLY!"
echo "========================================="
echo ""
echo "📍 Your application is ready at:"
echo "   Directory: /home/ubuntu/workspace"
echo ""
echo "🎬 Next steps:"
echo "   1. Review the code files"
echo "   2. Customize pricing in app.py if needed"
echo "   3. Deploy to Railway.app or Render.com"
echo "   4. See QUICK_START.md for deployment guide"
echo ""
echo "💡 Quick commands:"
echo "   Start server: source venv/bin/activate && python app.py"
echo "   Backup DB: python backup_db.py"
echo "   Health check: python health_check.py"
echo ""
echo "🌐 Deployment options:"
echo "   Option A: Railway.app (Recommended - Auto deploy)"
echo "   Option B: Render.com + Uptime Robot (Free forever)"
echo "   Option C: PythonAnywhere (100% free)"
echo ""
echo "📖 Documentation:"
echo "   - README.md - Quick overview"
echo "   - DEPLOYMENT.md - Hosting guides"
echo "   - FULL_GUIDE.md - Complete documentation"
echo "   - PANDUAN_LENGKAP.md - Indonesian guide"
echo "   - QUICK_START.md - Fast reference"
echo ""
echo "🎉 Good luck with your project!"
echo "========================================="
