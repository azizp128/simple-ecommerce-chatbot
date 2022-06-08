# Simple E-Commerce Chatbot
Simple E-Commerce Chatbot adalah sebuah Chatbot yang mampu memberikan respon kepada user terkait harga, penjualan, pembayaran, dan pengiriman berdasarkan intent yang sudah dikumpulkan.

Chatbot ini adalah project machine learning berbasis NLP yang dibuat menggunakan library tensorflow.

## How to Run
1. Install semua library yang ada di file requirements.txt menggunakan pip dengan perintah pip install -r requirements.txt
2. Uncomment line 4 jika belum pernah mendownload module "punkt"
3. Jalankan file predict.py dengan perintah python predict.py
4. Jalankan file gui.py jika ingin menjalankan program dalam versi GUI

Keterangan : 
Ketika menjalankan program melalui file predict.py maka program akan menampilkan 3 output yaitu respond bot, hasil klasifikasi jenis intent, dan hasil akurasi model pada setiap input user berdasarkan klasifikasi intent.
