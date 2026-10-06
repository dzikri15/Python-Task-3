# 🐍 Tugas Praktikum Pemrograman Python
**Mata Kuliah:** Pemrograman Python  
**Program Studi:** Sistem Informasi  
**Topik:** Logika Aplikasi — Variabel, I/O, Kondisional, Perulangan, dan Validasi Aturan Bisnis

---

## 📁 Daftar File

| No | File | Soal | Deskripsi |
|----|------|------|-----------|
| 1 | `status_mahasiswa.py` | Soal Praktik 1 | Laporan status 5 mahasiswa (Aktif / Peringatan / Tidak Aktif) |
| 2 | `diskon_biaya.py` | Soal Praktik 2 | Kalkulator diskon biaya kuliah |
| 3 | `peringatan_stok.py` | Soal Praktik 3 | Sistem peringatan stok inventaris |
| 4 | `menu_si_mahasiswa.py` | Soal Praktik 4 | Menu interaktif gabungan 3 studi kasus |
| 5 | `validasi_data.py` | Soal Praktik 5 | Validasi data mahasiswa |
| 6 | `ringkasan_algoritma.py` | Soal Praktik 6 | Ringkasan statistik algoritma |

---

## ▶️ Cara Menjalankan

Pastikan **Python 3** sudah terinstall. Cek dengan:
```bash
python --version
```

Jalankan masing-masing file dari terminal / PowerShell:

```bash
# Soal 1 - Status Mahasiswa
python status_mahasiswa.py

# Soal 2 - Diskon Biaya Kuliah
python diskon_biaya.py

# Soal 3 - Peringatan Stok
python peringatan_stok.py

# Soal 4 - Menu Interaktif
python menu_si_mahasiswa.py

# Soal 5 - Validasi Data
python validasi_data.py

# Soal 6 - Ringkasan Algoritma
python ringkasan_algoritma.py
```

> **Catatan:** Jalankan dari dalam folder `Tugas Py 3`, atau gunakan path lengkap.

---

## 📋 Penjelasan Program

### 1️⃣ `status_mahasiswa.py` — Laporan Status Mahasiswa
Program menerima input data **5 mahasiswa** (NIM, Nama, IPK, SKS) secara berulang menggunakan loop, lalu menampilkan laporan status akademik.

**Aturan bisnis:**
- ✅ **Aktif** → IPK ≥ 2.0 **DAN** SKS ≥ 18
- ⚠️ **Peringatan** → IPK 1.5 – 1.99
- ❌ **Tidak Aktif** → IPK < 1.5

**Input yang dibutuhkan:** NIM, Nama, IPK (0.0–4.0), SKS (0–24)

---

### 2️⃣ `diskon_biaya.py` — Kalkulator Diskon Biaya Kuliah
Program menghitung potongan biaya kuliah berdasarkan kategori mahasiswa.

**Aturan diskon (tidak kumulatif, ambil terbesar):**
| Kategori | Diskon |
|----------|--------|
| Anak Karyawan | 25% |
| IPK ≥ 3.8 (Prestasi Tinggi) | 20% |
| IPK ≥ 3.5 (Prestasi Baik) | 15% |
| IPK ≥ 3.0 (Memuaskan) | 10% |
| **Bayar Tepat Waktu** *(selalu ditambahkan)* | +5% |

**Input yang dibutuhkan:** Biaya SPP, anak karyawan (y/n), IPK, tepat waktu (y/n)

---

### 3️⃣ `peringatan_stok.py` — Sistem Peringatan Stok
Program mengevaluasi status stok **8 item** inventaris secara otomatis dan menghasilkan laporan lengkap.

**Level status stok:**
| Status | Kondisi | Prioritas |
|--------|---------|-----------|
| AMAN | Stok > 20 | LOW |
| PERINGATAN | Stok 11–20 | MEDIUM |
| RENDAH | Stok 1–10 | HIGH |
| HABIS | Stok = 0 | CRITICAL |

**Tidak memerlukan input** — data inventaris sudah tersedia di dalam program.

---

### 4️⃣ `menu_si_mahasiswa.py` — Menu Interaktif SI Mahasiswa
Program menu berbasis `while loop` yang menggabungkan ketiga studi kasus sebelumnya dalam satu antarmuka interaktif.

**Pilihan menu:**
```
1. Cek Status Mahasiswa
2. Hitung Diskon Biaya
3. Cek Peringatan Stok
0. Keluar
```

Semua input tervalidasi — program meminta ulang jika input tidak valid.

---

### 5️⃣ `validasi_data.py` — Validasi Data Mahasiswa
Program memvalidasi input data mahasiswa dan menampilkan daftar kesalahan jika ada.

**Aturan validasi:**
| Field | Aturan |
|-------|--------|
| NIM | 10 digit angka, tahun masuk 2000–2037 |
| IPK | Angka desimal 0.0 – 4.0 |
| SKS | Bilangan bulat 0 – 24 |
| Semester | Bilangan bulat 1 – 14 |

---

### 6️⃣ `ringkasan_algoritma.py` — Ringkasan Statistik
Program menghitung dan menampilkan ringkasan statistik dari ketiga studi kasus dalam format **tabel**.

**Output yang dihasilkan:**
- Persentase mahasiswa Aktif vs Tidak Aktif
- Rata-rata diskon yang diberikan
- Persentase item inventaris yang perlu restock

**Tidak memerlukan input** — menggunakan data simulasi bawaan.

---

## 🔑 Konsep Python yang Digunakan

- **Variabel & Tipe Data** — `str`, `int`, `float`, `bool`, `list`, `dict`
- **Input/Output** — `input()`, `print()`, f-string formatting
- **Kondisional** — `if`, `elif`, `else`
- **Perulangan** — `for`, `while`, `break`, `continue`
- **Fungsi** — `def`, parameter, return value
- **Validasi** — `try-except`, loop validasi, validasi komposit
- **Konstanta** — `UPPER_SNAKE_CASE` untuk aturan bisnis tetap
