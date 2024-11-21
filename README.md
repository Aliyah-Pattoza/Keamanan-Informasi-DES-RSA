Nama    : Andi Aliyah Nur Inayah Pattoza
NRP     : 5025221196
Kelas   : Keamanan Informasi (A)

## Tugas 3

Implementasi Pengiriman key DES pada percakapan menggunakan algoritma RSA

Program ini merupakan implementasi sederhana yang menggabungkan algoritma enkripsi RSA untuk pertukaran kunci dan algoritma DES untuk enkripsi pesan. Sistem ini menggunakan komunikasi client-server berbasis socket, di mana client mengirim pesan terenkripsi ke server dan menerima balasan terenkripsi. Server dan client berbagi kunci publik RSA untuk menukar kunci DES yang digunakan untuk mengenkripsi pesan-pesan selanjutnya.

### Fitur

- RSA untuk Pertukaran Kunci:

RSA digunakan untuk mengenkripsi kunci DES sebelum dikirim antara client dan server. Public key RSA server dikirim ke client, dan client menggunakan kunci tersebut untuk mengenkripsi kunci DES yang kemudian dikirim ke server.

- DES untuk Enkripsi Pesan:

Setelah kunci DES dibagikan, pesan-pesan selanjutnya dienkripsi dan didekripsi menggunakan algoritma DES. Proses ini memastikan komunikasi yang aman antara client dan server.

- Komunikasi Client-Server:

Client dan server saling bertukar pesan melalui socket. Setiap pesan yang dikirim dienkripsi menggunakan DES dan setiap balasan yang diterima didekripsi menggunakan kunci yang sama.

### Alur Program:

1. Koneksi:

- Client menghubungkan ke server melalui socket.
- Server mengirimkan public key RSA untuk memungkinkan client mengenkripsi kunci DES.

2. Enkripsi dan Dekripsi Pesan:

- Client mengenkripsi kunci DES menggunakan public key RSA dan mengirimkannya ke server.
- Client mengenkripsi pesan menggunakan kunci DES yang dibagikan, kemudian server mendekripsi pesan tersebut.
- Setelah itu, server dapat membalas dengan pesan yang juga dienkripsi menggunakan DES.

---

Program ini menggunakan library `rsa` untuk RSA enkripsi dan `socket` untuk komunikasi jaringan.

instalasi:

```
pip install rsa
```

setelah itu jalankan:

```
python3 server.py
```

dan 

```
python3 client.py
```

di terminal yang berbeda.

---

### Kesimpulan :

- RSA digunakan dalam program ini untuk mengenkripsi kunci DES yang digunakan untuk mengenkripsi pesan lebih lanjut. RSA adalah algoritma enkripsi berbasis kunci publik yang memungkinkan dua pihak untuk saling bertukar data secara aman meskipun mereka tidak pernah bertemu sebelumnya.

- PKA digunakan untuk pertukaran kunci rahasia antara client dan server yang digunakan untuk menghasilkan kunci DES bersama yang dapat digunakan untuk komunikasi selanjutnya.