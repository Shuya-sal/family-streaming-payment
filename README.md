# Aplikasi Pembayaran Netflix & YouTube Keluarga

## 🎬 Tentang Aplikasi
Aplikasi untuk mengelola pembayaran Netflix dan YouTube Premium untuk seluruh anggota keluarga dengan tracking otomatis.

## ✨ Fitur Utama
- ✅ Tracking otomatis setiap pembayaran anggota keluarga
- ✅ Pilihan durasi: 1, 2, 3, 6, atau 12 bulan
- ✅ Dashboard real-time untuk monitor semua transaksi
- ✅ Status subscription aktif/expired
- ✅ Riwayat pembayaran lengkap per anggota
- ✅ Notifikasi dan monitoring expiry
- ✅ Kode referensi unik untuk setiap pembayaran

## 🛠️ Teknologi
- Backend: Python Flask
- Database: SQLite (dapat upgrade ke PostgreSQL)
- Frontend: HTML5, CSS3, JavaScript
- Deployment: Render/Railway/PythonAnywhere

## 🚀 Instalasi Lokal

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Environment
```bash
# Copy .env file jika ada perubahan
cp .env.example .env
```

### 3. Jalankan Aplikasi
```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## 📱 Cara Menggunakan

### Untuk Admin:
1. Buka dashboard untuk melihat overview
2. Tambahkan anggota keluarga baru via `/register_member`
3. Monitor status payment dan subscription aktif

### Untuk Anggota Keluarga:
1. Setiap anggota akan memiliki ID unik
2. Klik "Bayar Sekarang" untuk membuat pembayaran
3. Pilih platform (Netflix/YouTube) dan durasi
4. Dapat kode referensi untuk tracking
5. Lihat riwayat pembayaran via tombol "Riwayat"

## 🌐 Deployment Gratis

### Option 1: Render.com (Recommended)
1. Push code ke GitHub repository
2. Buat akun di [render.com](https://render.com)
3. Create New → Web Service
4. Connect your GitHub repo
5. Configure:
   - Name: family-streaming-payment
   - Root Directory: .
   - Runtime: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -b 0.0.0.0:$PORT app:app`
6. Deploy! (Free tier tersedia, auto sleep setelah inactivity 15 menit)

### Option 2: Railway.app
1. Signup di [railway.app](https://railway.app)
2. Create new project
3. Deploy from GitHub
4. Set environment variables
5. Auto-deploy saat push ke main branch

### Option 3: PythonAnywhere
1. Create account di [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload files via web console
3. Configure WSGI configuration
4. Free domain: `<username>.pythonanywhere.com`

## 🔧 Environment Variables
```
FLASK_APP=app.py
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///family_payments.db
HOST=0.0.0.0
PORT=5000
```

## 📊 Pricing
- Netflix: Rp 75.000/bulan
- YouTube Premium: Rp 85.000/bulan

Dapat diubah di `app.py` pada fungsi `make_payment()`

## 🗄️ Database Schema

### Table: family_members
- id (Primary Key)
- name
- email (Unique)
- phone
- registered_at

### Table: payments
- id (Primary Key)
- member_id (Foreign Key)
- platform (Netflix/YouTube)
- duration_months
- amount
- payment_date
- start_date
- end_date
- status (active/expired)
- reference_code

## 🔒 Security Notes
- Ganti SECRET_KEY di production
- Gunakan HTTPS untuk production
- Backup database secara berkala
- Jangan commit `.env` ke git

## 📝 API Endpoints

### Public Pages
- `GET /` - Beranda
- `GET /register_member` - Form registrasi anggota
- `GET /dashboard` - Dashboard overview
- `GET /payment/<id>` - Form pembayaran

### API Routes
- `GET /api/members` - List semua members
- `GET /api/payment_status/<member_id>` - History payment per member
- `GET /api/summary` - Summary data (members, revenue, active subs)

## 🆘 Troubleshooting

### Masalah Database
Jika database bermasalah, hapus file `family_payments.db` dan restart aplikasi.

### Port Already in Use
Ubah port di terminal dengan:
```bash
export PORT=5001
python app.py
```

### Memory Issues
Gunakan gunicorn untuk production:
```bash
gunicorn -w 4 -b 0.0.0.0:$PORT app:app
```

## 💡 Customization
- Ubah harga di `app.py` line ~90
- Ubah warna theme di `static/css/style.css`
- Tambah metode pembayaran baru
- Integrasi dengan WhatsApp notification
- Email notification system

## 📞 Support
Untuk bantuan lebih lanjut, hubungi developer.

## 📜 License
MIT License - Free to use and modify

---
© 2024 Family Streaming Payment System
