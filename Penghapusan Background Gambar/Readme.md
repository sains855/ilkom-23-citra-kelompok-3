# Penghapusan Background Gambar

Proyek ini adalah aplikasi berbasis Python yang digunakan untuk menghapus background dari gambar menggunakan Flask dan rembg.

*Persyaratan*
Pastikan Anda memiliki Python terinstal di sistem Anda. Versi yang disarankan adalah **Python 3.8 atau lebih baru**.

*1. Membuat Virtual Environment (.venv)*
Untuk menjaga dependensi tetap terisolasi, gunakan *virtual environment*.

*Windows*
``
python -m venv .venv
.venv\Scripts\activate
``

*Linux/MacOS*
``
python3 -m venv .venv
source .venv/bin/activate
``

*2. Instalasi Dependensi*
Setelah mengaktifkan virtual environment, instal dependensi dengan:
``
pip install -r requirements.txt
``

Jika file `requirements.txt` belum ada, instal secara manual:
``
pip install flask rembg opencv-python
``

*3. Menjalankan `app.py`*
Pastikan virtual environment aktif, lalu jalankan aplikasi Flask dengan:
``
flask run
``
Atau jika menggunakan `app.py` sebagai entry point:
``
python app.py
``
Aplikasi akan berjalan di *http://127.0.0.1:5000/* secara default.

*4. Menonaktifkan Virtual Environment*
Setelah selesai, keluar dari virtual environment dengan:
``
deactivate
``
*Lisensi*
Proyek ini bersifat open-source dan bebas digunakan.
![Screenshot 2025-03-16 112627](https://github.com/user-attachments/assets/c144407d-ec08-4b14-a9ef-c32bc7fdd088)

