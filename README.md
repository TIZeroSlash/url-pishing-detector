### **README - URL Shortener & Phishing Detector**

---

### **Deskripsi Proyek**
Proyek ini adalah aplikasi web yang memungkinkan pengguna untuk:
1. **Memperpendek URL**: Mengubah URL panjang menjadi URL pendek.
2. **Mendeteksi Phishing**: Memeriksa URL yang dimasukkan apakah mengandung ancaman phishing menggunakan **Google Safe Browsing API**.
3. **Statistik URL**: Menyediakan statistik seperti jumlah klik, waktu terakhir diakses, dan waktu pembuatan untuk setiap URL pendek.

---

### **Fitur Utama**
1. **URL Shortening**:
   - URL panjang diubah menjadi kode pendek (e.g., `https://example.com/abcd12`).
2. **Phishing Detection**:
   - URL dicek terhadap Google Safe Browsing API untuk mendeteksi ancaman phishing (e.g., malware, social engineering).
   - URL yang terdeteksi phishing tidak akan diizinkan untuk diperpendek.
3. **URL Validation**:
   - URL diperiksa apakah aktif dan dapat dijangkau.
4. **Statistics Endpoint**:
   - Menyediakan statistik seperti jumlah klik, waktu terakhir diakses, dan waktu pembuatan.

---

### **Alur Logika**
1. **Input URL**:
   - Pengguna memasukkan URL ke form.
2. **Phishing Check**:
   - URL diperiksa terhadap **Google Safe Browsing API**:
     - Jika terindikasi phishing: tampilkan pesan error.
3. **Validation Check**:
   - URL diperiksa apakah aktif menggunakan permintaan `HEAD`.
     - Jika URL tidak valid atau tidak dapat dijangkau: tampilkan pesan error.
4. **URL Shortening**:
   - Jika URL valid dan aman, generate kode pendek untuk URL.
   - Simpan URL asli dan kode pendek dalam memori (`url_map`).
   - Simpan statistik awal untuk URL pendek dalam memori (`url_stats`).
5. **Statistics**:
   - Statistik disediakan pada endpoint `/stats/<short_code>` untuk setiap URL pendek.
   - Statistik mencakup:
     - Jumlah klik
     - Waktu terakhir diakses
     - Waktu pembuatan URL pendek.

---

### **Struktur File**
```
.
├── app.py                 # Main Flask application
├── .env                   # Environment variables (Google API Key)
├── templates/
│   └── index.html         # HTML template untuk halaman utama
├── static/
│   └── style.css          # Style untuk aplikasi
└── requirements.txt       # Dependency Python
```

---

### **Cara Menggunakan**
1. **Setup Environment**:
   - Buat file `.env` di direktori root dengan isi:
     ```
     GOOGLE_API_KEY=your_google_safe_browsing_api_key
     ```
   - Ganti `your_google_safe_browsing_api_key` dengan API key Anda.

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi**:
   ```
   python app.py
   ```
   Aplikasi akan berjalan di `http://127.0.0.1:5000/`.

4. **Deploy di Server (Optional)**:
   - Gunakan layanan seperti **PythonAnywhere** atau server VPS.
   - Pastikan API key dan dependencies sudah diatur.

5. **Gunakan Aplikasi**:
   - Buka aplikasi di browser.
   - Masukkan URL pada form input.
   - Jika URL valid dan aman:
     - Dapatkan **Shortened URL** dan **Stats URL**.
   - Jika URL tidak valid:
     - Tampilkan pesan error.

---

### **Endpoint API**
1. **Halaman Utama** (`/`):
   - **Method**: `GET` / `POST`
   - **Fungsi**: Memasukkan URL dan mendapatkan Shortened URL.
2. **Redirect URL** (`/<short_code>`):
   - **Method**: `GET`
   - **Fungsi**: Redirect ke URL asli berdasarkan short code.
3. **Statistik URL** (`/stats/<short_code>`):
   - **Method**: `GET`
   - **Fungsi**: Menampilkan statistik untuk URL pendek.

---

### **Statistik URL**
Untuk setiap URL pendek, statistik mencakup:
- **Jumlah Klik**: Berapa kali URL pendek telah diakses.
- **Waktu Pembuatan**: Waktu saat URL pendek dibuat.
- **Waktu Terakhir Diakses**: Waktu terakhir URL pendek diakses.

---

### **Pesan Error**
1. **Phishing URL Detected**:
   - Pesan: *"Phishing URL terdeteksi! Mohon masukkan URL yang aman."*
   - Penanganan: URL tidak diperpendek.
2. **Invalid URL**:
   - Pesan: *"URL tidak valid atau tidak dapat dijangkau. Coba masukkan URL lain."*
   - Penanganan: URL tidak diperpendek.
3. **Empty Input**:
   - Pesan: *"Mohon masukkan URL terlebih dahulu."*
   - Penanganan: Tidak ada aksi, pesan ditampilkan.

---

### **Catatan Tambahan**
- **Google API Key**:
  - API Key wajib untuk mengakses Google Safe Browsing API.
  - Pastikan key valid dan memiliki izin.
- **In-Memory Storage**:
  - URL dan statistik disimpan dalam memori (RAM).
  - Jika server restart, semua data akan hilang. Untuk produksi, gunakan database seperti SQLite, PostgreSQL, atau MongoDB.

---

### **Kontak**
Jika ada pertanyaan atau butuh bantuan, silakan kunjungi profil saya:  
[**Muhammad Andyk Maulana**](https://muhammadandykmaulana.github.io)  

---

### **Lisensi**
Proyek ini berlisensi **MIT**. Anda bebas menggunakan, memodifikasi, dan mendistribusikan proyek ini dengan mencantumkan atribusi kepada penulis asli.
