# 🚀 QUICK START - FAMILY STREAMING PAYMENT SYSTEM

## ⚡ SUPER CEPAT DEPLOY (5 MENIT)!

### STEP 1: Setup Git Repository
```bash
cd /home/ubuntu/workspace
git init
git add .
git commit -m "Initial family streaming payment system"
git branch -M main
```

### STEP 2: Push to GitHub
```bash
# Buat repo baru di github.com/new
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git push -u origin main
```

### STEP 3: Deploy ke Railway.app (PALING MUDAH!)
1. Buka: https://railway.app
2. Sign up dengan GitHub
3. New Project → "Deploy from GitHub repo"
4. Pilih repository Anda
5. CLICK DEPLOY!

✅ **DONE!** App live dalam 2 menit, ALWAYS ON!

---

## 📍 CARA MENGGUNAKAN APLIKASI:

### Akses Aplikasi:
```
http://YOUR-APP-URL.onrailway.app
```

### Flow Penggunaan:

1. **Tambah Anggota Keluarga**
   - Dashboard → "Tambah Anggota"
   - Isi nama, email
   - Simpan

2. **Bayar Netflix/YouTube**
   - Pilih member yang akan dibayar
   - Klik "Bayar Sekarang"
   - Pilih platform & durasi
   - Submit → Dapat kode referensi!

3. **Monitor Status**
   - Dashboard menampilkan semua info real-time
   - Click "Riwayat" untuk lihat transaksi lengkap

---

## 💰 PRICING DEFAULT:

- **Netflix:** Rp 75.000/bulan
- **YouTube Premium:** Rp 85.000/bulan

Bisa diubah di `app.py` line ~90

---

## 🔧 CUSTOMIZATION CEPAT:

### Ubah Harga
Edit `/home/ubuntu/workspace/app.py`:
```python
price_per_month = {
    'Netflix': 100000,        # Ganti harga disini
    'YouTube Premium': 95000  # Ganti harga disini
}
```

### Tambah Platform
Di `app.py`, cari baris `platforms = [...]` dan tambahkan platform baru.

---

## 📊 MONITORING:

### Check Server Status
```bash
python health_check.py
```

### Backup Database
```bash
python backup_db.py
```

---

## ❗ TROUBLESHOOTING:

**Server tidak jalan?**
```bash
# Cek logs di dashboard hosting platform
# Atau restart deployment
```

**Database error?**
```bash
rm family_payments.db
python app.py  # Fresh start
```

---

## 🎯 DONE! 

Sekarang tinggal:
1. ✅ Invite family members via WhatsApp/Email
2. ✅ Share aplikasi URL mereka
3. ✅ Monitor pembayaran via dashboard
4. ✅ Enjoy! 🎉

---

**Cost:** $0 FREE  
**Uptime:** 100%  
**Setup Time:** 5 menit

**Happy Streaming! 🍿📺**

