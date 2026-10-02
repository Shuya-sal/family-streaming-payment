# 🎬 FAMILY STREAMING PAYMENT SYSTEM
## Aplikasi Pembayaran Netflix & YouTube Premium Untuk Keluarga

---

## 🌟 FITUR UTAMA

### ✅ Sistem Tracking Otomatis
- Setiap pembayaran anggota keluarga tercatat otomatis di database
- Status subscription aktif/expired termonitor real-time
- Kode referensi unik untuk setiap transaksi

### ✅ Fleksibilitas Durasi Pembelian
- 1 bulan (Rp 75.000/bulan)
- 2 bulan 
- 3 bulan
- 6 bulan
- 12 bulan

### ✅ Dashboard Monitoring
- Ringkasan total member dan pendapatan
- List semua anggota keluarga dengan status payment
- History pembayaran lengkap per member
- Alert untuk subscription即将 expired

### ✅ API Lengkap
- RESTful API untuk integrasi
- Endpoint untuk get members, payments, summary
- JSON response format

---

## 📁 STRUKTUR FILE

```
family-streaming-payment/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment config
├── .env                  # Environment variables
├── .gitignore           # Git ignore rules
├── backup_db.py         # Database backup script
├── health_check.py      # Health monitoring script
├── scheduler_config.txt # Cron/systemd configuration guide
│
├── templates/           # HTML templates
│   ├── index.html               # Home page
│   ├── register_member.html     # Member registration form
│   ├── make_payment.html        # Payment form
│   ├── payment_success.html     # Success page
│   └── dashboard.html           # Dashboard overview
│
├── static/css/        # CSS styles
│   └── style.css
│
└── systemd/           # Systemd service files
    ├── family-payment-backup.service
    └── family-payment-backup.timer
```

---

## 🚀 QUICK START

### Local Development

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Set Environment Variables**
```bash
export FLASK_APP=app.py
export FLASK_ENV=production
export SECRET_KEY="your-secret-key-here"
```

3. **Run Application**
```bash
python app.py
```

4. **Access at** http://localhost:5000

---

## 🌐 DEPLOYMENT FREE HOSTING

### Option 1: Render.com ⭐ RECOMMENDED

**Cost:** FREE (auto-sleep after 15 min inactivity)  
**Uptime Solution:** Uptime Robot ping every 10 minutes

**Step-by-step:**

1. Push code to GitHub
```bash
cd /home/ubuntu/workspace
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/family-streaming-payment.git
git push -u origin main
```

2. Deploy ke Render
   - Visit render.com/signup
   - New → Web Service
   - Connect GitHub repository
   - Settings:
     - Name: family-streaming-payment
     - Branch: main
     - Runtime: Python
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn -b 0.0.0.0:$PORT app:app`
   - Advanced → Add Env Var: `PORT=5000`
   - Create!

3. Setup auto-wakeup with UptimeRobot
   - Sign up at uptimerobot.com
   - Add new monitor → HTTP(s)
   - URL: your-render-url.herokuapp.com
   - Check every 10 minutes
   - Save!

✅ App akan live dalam ~2 menit

---

### Option 2: Railway.app 💰 Always On

**Cost:** $5/month free credit (always on!)  
**Uptime:** No sleep mode

**Steps:**
1. Visit railway.app/signup
2. Login with GitHub
3. New Project → Deploy from GitHub repo
4. Select your repository
5. Railway auto-detects everything
6. Click Deploy

✅ Instant deployment!

---

### Option 3: PythonAnywhere 🆓 Forever Free

**Cost:** 100% FREE forever  
**Uptime:** Always on on free tier

**Steps:**
1. Sign up at pythonanywhere.com
2. Console tab → Upload files via git:
```bash
git clone YOUR_REPO_URL
cd family-streaming-payment
```
3. Websites tab → Add website
4. Choose WSGI configuration
5. Point to your project directory

✅ Domain: YOURNAME.pythonanywhere.com

---

### Option 4: Huggerson.fyi 🚀 Free + Fast

**Cost:** FREE  
**Uptime:** Always on  
**Speed:** Very fast servers

**Steps:**
1. Visit hugerson.fyi
2. Fork their Python template
3. Connect GitHub repository
4. Deploy instantly

✅ Fastest free option!

---

## 🛠️ CUSTOMIZATION

### Change Pricing
Edit `/home/ubuntu/workspace/app.py` line ~90:
```python
price_per_month = {
    'Netflix': 75000,        # Change here
    'YouTube Premium': 85000 # Change here
}
```

### Customize Platform
Add more platforms:
```python
platforms = ['Netflix', 'YouTube Premium', 'Disney+', 'HBO Go']
```

Update the `make_payment` function to handle new platforms.

### Custom Email Notifications
Integrate with SMTP for email alerts when subscription expires:
```python
import smtplib
from email.mime.text import MIMEText

def send_expiry_alert(member_email, expiry_date):
    # Add your SMTP configuration
    pass
```

---

## 🔒 SECURITY NOTES

1. **Always change SECRET_KEY** in production
2. **Enable HTTPS** (most platforms provide SSL automatically)
3. **Don't share admin links** publicly
4. **Backup database regularly** (use provided backup script)
5. **Use environment variables** for sensitive data

---

## 📊 MONITORING & BACKUP

### Manual Backup
```bash
python backup_db.py
```
Creates backup in `/backups/` folder with timestamp

### Automatic Daily Backup (Linux)
```bash
crontab -e
# Add: 0 0 * * * cd /home/ubuntu/workspace && python3 backup_db.py >> logs/backup.log 2>&1
```

### Health Check
```bash
python health_check.py
```
Shows stats and potential issues

---

## 📱 API ENDPOINTS

### Pages
- `GET /` - Home page
- `GET /dashboard` - Dashboard overview
- `POST /register_member` - Register new member
- `GET /payment/<id>` - Payment form
- `POST /payment/<id>` - Process payment

### API Routes
- `GET /api/members` - JSON list of all members
- `GET /api/payment_status/<member_id>` - Payment history per member
- `GET /api/summary` - Summary statistics (JSON)

Example API Response:
```json
{
  "total_members": 5,
  "payments_this_month": 12,
  "total_revenue_this_month": 945000,
  "active_subscriptions": 4,
  "subscription_value": 315000
}
```

---

## 🗄️ DATABASE SCHEMA

### Table: family_members
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PRIMARY KEY | Auto-increment ID |
| name | TEXT NOT NULL | Member name |
| email | TEXT UNIQUE | Email address |
| phone | TEXT | Phone number (optional) |
| registered_at | TIMESTAMP | Registration time |

### Table: payments
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PRIMARY KEY | Auto-increment ID |
| member_id | INTEGER FK | Reference to member |
| platform | TEXT | Netflix or YouTube |
| duration_months | INTEGER | Duration selected |
| amount | REAL | Total paid |
| payment_date | TIMESTAMP | When paid |
| start_date | DATE | Subscription starts |
| end_date | DATE | Subscription ends |
| status | TEXT | active or expired |
| reference_code | TEXT | Unique transaction ID |

---

## 🧪 TESTING

### Test Locally
```bash
python app.py
# Open http://localhost:5000
# Try adding a member
# Try making a payment
# Check dashboard
```

### Test API
```bash
curl http://localhost:5000/api/members
curl http://localhost:5000/api/summary
curl http://localhost:5000/api/payment_status/1
```

---

## 🐛 TROUBLESHOOTING

### Issue: Port Already in Use
```bash
export PORT=5001
python app.py
```

### Issue: Database Error
```bash
rm family_payments.db
python app.py  # Will recreate fresh database
```

### Issue: Import Error
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: Server Won't Start
Check error logs:
```bash
tail -f logs/error.log
```

---

## 📞 SUPPORT & CONTRIBUTION

### Need Help?
- Read FULL documentation in README.md
- Check DEPLOYMENT.md for hosting guides
- Review code comments in app.py

### Want to Contribute?
1. Fork repository
2. Create feature branch
3. Make changes
4. Submit pull request

---

## 📝 LICENSE

MIT License - Free to use and modify for personal or commercial projects

---

## 🙏 CREDITS

Built with ❤️ using Flask framework

Special thanks to:
- Flask team for amazing framework
- Render/Railway/PythonAnywhere for free hosting
- SQLite for lightweight database

---

## 🔥 FUTURE FEATURES (Roadmap)

- [ ] WhatsApp/SMS notifications
- [ ] Email alerts before expiration
- [ ] Multiple currency support
- [ ] Admin panel with authentication
- [ ] Mobile app (React Native/Flutter)
- [ ] Stripe/Payment gateway integration
- [ ] Analytics dashboard
- [ ] Multi-language support

---

**Version:** 1.0.0  
**Last Updated:** 2024  
**Status:** Production Ready ✅

---

Made with ❤️ for families worldwide 🌍
