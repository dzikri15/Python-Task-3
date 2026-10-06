# Jawaban Soal Teori - Modul Praktikum Logika Aplikasi

## 1. Aturan bisnis vs logika teknis
**Aturan bisnis** adalah kebijakan organisasi yang ditulis dalam bahasa bisnis dan berubah mengikuti kebijakan. **Logika teknis** adalah mekanisme implementasi agar program berjalan dan tidak bergantung pada kebijakan.

- Aturan bisnis: (1) mahasiswa Aktif jika IPK >= 2.0 dan SKS >= 18; (2) diskon 25% untuk anak karyawan.
- Logika teknis: (1) mengonversi hasil `input()` dari `str` ke `float`; (2) menyimpan data mahasiswa dalam `dict` dan memprosesnya dengan `for` loop.

## 2. NIM sebagai string
NIM adalah identitas (label), bukan bilangan untuk dihitung. Jika disimpan sebagai `int`:
- angka nol di depan hilang (`"0021001"` menjadi `21001`) sehingga NIM berubah;
- format dan panjang tidak bisa dicek dengan `len()` / `isdigit()` / slicing tahun masuk;
- tidak masuk akal diperlakukan secara aritmetika (NIM + 1 tidak bermakna).

## 3. `and` vs `or`
- `and`: True hanya jika **semua** kondisi True. Contoh: Aktif jika `ipk >= 2.0 and sks >= 18 and not is_cuti`.
- `or`: True jika **salah satu** kondisi True. Contoh: layak diskon jika `is_anak_karyawan or ipk >= 3.8`.
- Precedence: `not` dievaluasi sebelum `and`, `and` sebelum `or`. Gunakan kurung agar jelas.

## 4. Urutan kondisi di if-elif-else
Kondisi dievaluasi dari atas ke bawah dan hanya blok pertama yang True yang dijalankan. Jika kondisi umum ditaruh sebelum yang spesifik, kondisi spesifik tidak pernah tercapai. Contoh: `if nilai >= 45` ditaruh paling atas membuat nilai 90 ikut jatuh ke grade D, bukan A. Susun dari ambang tertinggi ke terendah (atau dari yang paling spesifik).

## 5. `for` vs `while`
- `for`: jumlah iterasi diketahui atau ada koleksi untuk ditelusuri. Contoh: menghitung status setiap mahasiswa dalam daftar, total SPP 8 semester.
- `while`: jumlah iterasi tidak diketahui, bergantung kondisi. Contoh: menu interaktif sampai pengguna memilih keluar, input ulang sampai IPK valid.

## 6. `else` pada loop
`else` pada `for`/`while` dijalankan **hanya jika loop selesai normal (tanpa `break`)**. Contoh: setelah mencari stok kritis, `else` mencetak "semua stok aman" jika tidak ada `break`. Pada `if-else`, `else` dijalankan jika kondisi `if` False, tidak terkait `break`.

## 7. Mengapa validasi sebelum aturan bisnis
Aturan bisnis mengasumsikan data benar. Tanpa validasi:
- program crash (`ValueError` saat `float("abc")`);
- keputusan salah (IPK 5.0 dianggap sah, status/diskon keliru);
- data tidak konsisten tersimpan, dan lebih mahal diperbaiki belakangan.

## 8. Validasi komposit
Validasi komposit memeriksa beberapa kondisi sekaligus dan mengumpulkan pesan error untuk setiap syarat yang gagal. Contoh beasiswa:

```python
def cek_beasiswa(mhs):
    errors = []
    if mhs["ipk"] < 3.5:
        errors.append("IPK minimal 3.5")
    if mhs["semester"] < 3:
        errors.append("Minimal semester 3")
    if mhs["tunggakan"] > 0:
        errors.append("Masih ada tunggakan biaya")
    if mhs["penghasilan_ortu"] > 5_000_000:
        errors.append("Penghasilan orang tua melebihi batas")
    return (not errors), errors
```
