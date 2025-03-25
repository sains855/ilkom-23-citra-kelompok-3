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


![Screenshot 2025-03-16 112627](https://github.com/user-attachments/assets/c144407d-ec08-4b14-a9ef-c32bc7fdd088)



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

### *Proses Menghapus Background Gambar dengan Rembg (Remove Background)* 

Alur kerja untuk menghapus background gambar menggunakan **rembg** dan model **U2Net**:  

*a. Instalasi Rembg*
Sebelum digunakan, pastikan *rembg* sudah terinstal.  
Jalankan perintah berikut di terminal:  
``
pip install rembg
``
*b. Unduh Model U2Net* 
- Ketika pertama kali menjalankan *rembg*, sistem akan mengunduh model *U2Net* (seperti yang terlihat di terminal pada gambar yang kamu berikan).  
- Model ini digunakan untuk mendeteksi dan menghapus background gambar.

*c. Menghapus Background Gambar* 
Setelah model terunduh, gunakan perintah berikut untuk menghapus background gambar:  
``
rembg i input.jpg output.png
``
- *`input.jpg`* → Gambar asli yang ingin dihapus background-nya.  
- *`output.png`* → Hasil gambar dengan background transparan.

*d. Hasil Akhir*  
- Gambar output akan memiliki *background transparan*.  
- Format output biasanya dalam *PNG* karena mendukung transparansi.

Rembg bekerja dengan *model deep learning U2Net* yang dapat mendeteksi objek utama dalam gambar dan menghapus latar belakangnya secara otomatis.

*4. Menonaktifkan Virtual Environment*
Setelah selesai, keluar dari virtual environment dengan:
``
deactivate
``
*Lisensi*
Proyek ini bersifat open-source dan bebas digunakan.
