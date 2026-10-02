# Setup Script for Family Streaming Payment System

echo "========================================"
echo "🎬 Family Streaming Payment System - Setup"
echo "========================================"
echo ""

# Check Python version
echo "Step 1: Checking Python version..."
python3 --version

echo ""
echo "Step 2: Creating virtual environment..."
cd /home/ubuntu/workspace
python3 -m venv venv
source venv/bin/activate

echo ""
echo "Step 3: Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Step 4: Setting up environment variables..."
if [ ! -f .env ]; then
    echo "# Create your .env file with these values:"
    echo "FLASK_APP=app.py"
    echo "FLASK_ENV=production"
    echo "SECRET_KEY=your-random-secret-key-generate-this-with-python"
    echo "DATABASE_URL=sqlite:///family_payments.db"
else
    echo ".env file already exists"
fi

echo ""
echo "Step 5: Testing the application..."
python3 app.py &
sleep 3
curl http://localhost:5000 > /dev/null && echo "✅ Server is running on port 5000!" || echo "❌ Server failed to start"

echo ""
echo "Step 6: Cleanup background process"
pkill -f "python3 app.py" || true

echo ""
echo "========================================"
echo "✅ Setup complete! Next steps:"
echo "========================================"
echo "1. Start server: source venv/bin/activate && python3 app.py"
echo "2. Access at: http://localhost:5000"
echo "3. Deploy to Render/Railway (see README.md)"
echo ""
