import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ===================================================================
# KONFIGURASI - Semua informasi diatur di sini 465 / 587
# ===================================================================
SMTP_HOST = ""
SMTP_PORT = 587 
SMTP_USERNAME = ""
SMTP_PASSWORD = ""  # PERINGATAN: Kredensial sensitif ada di sini
SENDER_EMAIL = ""
# ===================================================================

def send_email(recipient_email, subject, html_content, text_content):
    """
    Mengirim email menggunakan konfigurasi yang sudah di-hardcode di dalam skrip.

    Args:
        recipient_email (str): Alamat email penerima.
        subject (str): Subjek email.
        html_content (str): Isi email dalam format HTML.
        text_content (str): Isi email dalam format teks biasa (sebagai fallback).

    Returns:
        bool: True jika email berhasil dikirim, False jika gagal.
    """
    # Membuat Pesan Email (MIMEMultipart)
    # "alternative" berarti klien email akan memilih antara teks biasa dan HTML
    message = MIMEMultipart("alternative")
    message["From"] = SENDER_EMAIL
    message["To"] = recipient_email
    message["Subject"] = subject

    # Lampirkan kedua versi: teks biasa dan HTML
    # Penting: Lampirkan versi teks biasa terlebih dahulu
    part1 = MIMEText(text_content, "plain")
    part2 = MIMEText(html_content, "html")
    
    message.attach(part1)
    message.attach(part2)

    # Menghubungkan ke Server dan Mengirim Email
    try:
        # Menggunakan 'with' memastikan koneksi ditutup secara otomatis
        print(f"Menghubungkan ke server {SMTP_HOST}:{SMTP_PORT}...")
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()  # Mengaktifkan keamanan TLS
            print(f"Login dengan username '{SMTP_USERNAME}'...")
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            print("Login berhasil. Mengirim email...")
            server.sendmail(
                SENDER_EMAIL, recipient_email, message.as_string()
            )
            print(f"Email berhasil dikirim ke {recipient_email}!")
            return True
            
    except smtplib.SMTPAuthenticationError:
        print("Kesalahan: Autentikasi gagal. Periksa kembali username dan password SMTP Anda.")
        return False
    except smtplib.SMTPServerDisconnected:
        print("Kesalahan: Koneksi ke server terputus. Periksa kembali host dan port SMTP.")
        return False
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")
        return False

# Bagian ini hanya berjalan jika skrip dieksekusi secara langsung
if __name__ == "__main__":
    print("===== Menjalankan Skrip Pengujian Email =====")
    
    # Contoh data untuk pengujian
    test_recipient = ""  # Ganti dengan email tujuan Anda
    test_subject = "Email Percobaan dari Skrip Python"
    
    # Isi email versi teks biasa (untuk klien email lama)
    test_plain_text = """
    Halo,
    Ini adalah email percobaan yang dikirim dari satu file Python.
    Jika Anda melihat ini, berarti klien email Anda tidak mendukung HTML.
    Terima kasih.
    """
    
    # Isi email versi HTML (lebih menarik secara visual)
    test_html_text = """
    <html>
    <body>
        <h2 style="color:#007BFF;">Halo!</h2>
        <p>Ini adalah email percobaan yang dikirim dari <b>satu file Python</b>.</p>
        <p>Email ini mendukung format HTML, sehingga bisa menyertakan:</p>
        <ul>
            <li>Teks tebal dan miring</li>
            <li>Daftar (list)</li>
            <li><a href="https://www.google.com">Tautan (link)</a></li>
        </ul>
        <p style="font-size:12px; color:grey;">Terima kasih.</p>
    </body>
    </html>
    """
    
    # Memanggil fungsi untuk mengirim email
    success = send_email(
        recipient_email=test_recipient,
        subject=test_subject,
        html_content=test_html_text,
        text_content=test_plain_text
    )
    
    if success:
        print("\n===== Proses selesai dengan sukses. =====")
    else:
        print("\n===== Proses gagal. Periksa pesan error di atas. =====")