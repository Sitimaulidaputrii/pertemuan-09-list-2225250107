# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Siti Maulida Putri Irawan
NIM: 2225250107
Kelas: 3A

## Tujuan

Memahami penggunaan list Python untuk menyimpan dan mengolah kumpulan nilai numerik. Program ini digunakan untuk menghitung jumlah data, total, rata-rata, nilai minimum dan maksimum, serta menentukan jumlah mahasiswa yang lulus dan belum lulus.

## Struktur Program

1. latihan/01_buat_list.py: Membuat list dan membaca data yang tersimpan di dalamnya.
2. latihan/02_indeks_slicing.py: Mempelajari cara mengakses elemen list menggunakan indeks dan slicing.
3. latihan/03_manipulasi_list.py: Mempelajari cara mengubah, menambahkan, menyisipkan, dan menghapus elemen list.
4. latihan/04_agregasi_nilai.py: Menghitung total, rata-rata, nilai minimum, dan nilai maksimum dari data numerik.
5. latihan/05_filter_kelulusan.py: Memilih nilai yang memenuhi batas kelulusan 60 dan menghitung jumlah nilai yang lulus.
6. latihan/06_fungsi_statistik.py: Membuat fungsi untuk menghitung rata-rata dan menangani list kosong.
7. praktik/analisis_nilai_mahasiswa.py: Mengolah data nilai mahasiswa untuk menampilkan statistik nilai serta menentukan jumlah mahasiswa yang lulus dan belum lulus.

## Cara Menjalankan

Program praktik dapat dijalankan melalui Terminal VS Code dengan perintah:
```bash
Python praktik/analisis_nilai_mahasiswa.py
```

untuk menjalankan program latihan:
```bash
python latihan/01_buat_list.py
```

untuk menjalankan yang lainnya, gunakan perintah sesuai dengan nama berkasnya.

## Test Case

| Data | Hasil yang diharapkan | Hasil aktual | Status |
| --- | --- | --- | --- |
| [60, 70, 80] Rata-rata | 70.00 | 70.0 | Berhasil |
| [60, 70, 80] Minimum/Maksimum | 60/80 | 60, 80 | Berhasil |
| [60, 70, 80] Jumlah lulus | 3 | 3 | Berhasil |
| [59, 60, 61] Batas kelulusan | 2 lulus | [60, 61] (2 lulus) | Berhasil |
| [] Penanganan list kosong pada fungsi rata-rata | Tidak error | 0 | Berhasil |

## Refleksi

Saya memahami bahwa list dapat digunakan untuk menyimpan banyak nilai dalam satu variabel. Salah satu kesalahan yang berhasil saya perbaiki adalah memastikan saat mengumpulkan nilai mahasiswa yang lulus ke dalam list baru, saya belajar menggunakan append() untuk memasukkan nilai yang memenuhi batas kelulusan.

## Referensi  

Materi pertemuan 07 Algoritma dan Pemrograman: List/Array dan Pengolahan Data Numerik Sederhana.
Python Software Foundation. The Python Tutorial.