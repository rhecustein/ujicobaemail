# Skrip Pengirim Email SMTP dengan Python

Sebuah skrip Python sederhana untuk mengirim email melalui server SMTP. Skrip ini dirancang agar mudah dikonfigurasi dan dijalankan untuk pengujian cepat atau tugas pengiriman email otomatis.

Skrip ini mendukung pengiriman email dalam format HTML dengan fallback ke format teks biasa, memastikan kompatibilitas di berbagai klien email.

## Fitur
- Mengirim email melalui koneksi SMTP yang aman menggunakan `STARTTLS`.
- Mendukung format email HTML dan Teks Biasa (Multipart/Alternative).
- Struktur fungsi yang bersih dan mudah digunakan kembali (`send_email`).
- Konfigurasi terpusat di dalam satu file untuk kemudahan pengujian cepat.

## Prasyarat
- **Python 3.x**

Tidak ada library eksternal yang perlu diinstal, karena semua modul yang digunakan (`smtplib`, `email`) adalah bagian dari Pustaka Standar Python.

## Konfigurasi
Sebelum menjalankan skrip, Anda harus mengisi detail konfigurasi SMTP Anda langsung di dalam file skrip Python.

Buka file skrip dan temukan bagian `KONFIGURASI`. Ganti nilai placeholder dengan informasi Anda yang sebenarnya.

```python
# ===================================================================
# KONFIGURASI - Semua informasi diatur di sini
# ===================================================================
SMTP_HOST = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_email_password_or_app_password" # PERINGATAN: Kredensial sensitif ada di sini
SENDER_EMAIL = "your_email@example.com"
# ===================================================================
```

**Catatan Penting:**
- `SMTP_HOST`: Alamat server SMTP provider email Anda (misalnya, `smtp.gmail.com`).
- `SMTP_PORT`: Port yang digunakan untuk koneksi SMTP (biasanya `587` untuk TLS atau `465` untuk SSL).
- `SMTP_PASSWORD`: Untuk beberapa layanan seperti Gmail, Anda mungkin perlu membuat **"App Password"** alih-alih menggunakan password utama akun Anda.

Anda juga perlu mengatur email penerima untuk pengujian di bagian bawah file:

```python
if __name__ == "__main__":
    # ...
    test_recipient = "recipient_email@example.com"  # Ganti dengan email tujuan Anda
    # ...
```

## Cara Menjalankan
1. Pastikan Anda telah mengisi semua detail pada bagian `KONFIGURASI` di dalam file skrip.
2. Buka terminal atau command prompt.
3. Navigasi ke direktori tempat Anda menyimpan file tersebut.
4. Jalankan skrip dengan perintah:
   ```bash
   python nama_file_anda.py
   ```

## ⚠️ Peringatan Keamanan
Skrip ini menyimpan kredensial (username dan password) secara langsung di dalam kode sumber untuk kemudahan.

**Praktik ini sangat tidak aman** dan tidak direkomendasikan untuk lingkungan produksi, kode yang dibagikan, atau proyek apa pun yang akan disimpan di repositori publik (seperti GitHub). Siapa pun yang memiliki akses ke file kode sumber akan dapat melihat kata sandi Anda dalam bentuk teks biasa.

Untuk penggunaan yang lebih aman dalam proyek nyata, pertimbangkan untuk menyimpan informasi sensitif menggunakan **Environment Variables**.

## Lisensi
Proyek ini dilisensikan di bawah [Lisensi MIT](LICENSE).
