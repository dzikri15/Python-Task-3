"""Soal Praktik 2 - Kalkulator diskon biaya kuliah."""

DISKON_ANAK_KARYAWAN = 0.25
DISKON_PRESTASI_TINGGI = 0.20   # IPK >= 3.8
DISKON_PRESTASI_BAIK = 0.15     # IPK >= 3.5
DISKON_MEMUASKAN = 0.10         # IPK >= 3.0
DISKON_TEPAT_WAKTU = 0.05       # tambahan, selalu ditambahkan


def baca_angka(prompt, tipe, minimum, maksimum):
    while True:
        try:
            nilai = tipe(input(prompt))
        except ValueError:
            print("  Error: masukkan angka yang valid")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Error: nilai harus antara {minimum} dan {maksimum}")


def baca_ya_tidak(prompt):
    while True:
        jawab = input(prompt).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  Error: jawab dengan y atau n")


def hitung_diskon(ipk, is_anak_karyawan, is_tepat_waktu):
    """Diskon utama tidak kumulatif (ambil satu yang berlaku),
    diskon tepat waktu selalu ditambahkan."""
    if is_anak_karyawan:
        utama, kategori = DISKON_ANAK_KARYAWAN, "Anak Karyawan"
    elif ipk >= 3.8:
        utama, kategori = DISKON_PRESTASI_TINGGI, "Prestasi Tinggi"
    elif ipk >= 3.5:
        utama, kategori = DISKON_PRESTASI_BAIK, "Prestasi Baik"
    elif ipk >= 3.0:
        utama, kategori = DISKON_MEMUASKAN, "IPK Memuaskan"
    else:
        utama, kategori = 0.0, "Tidak ada diskon utama"
    tambahan = DISKON_TEPAT_WAKTU if is_tepat_waktu else 0.0
    return utama, tambahan, kategori


def main():
    print("=== Kalkulator Diskon Biaya Kuliah ===")
    biaya = baca_angka("Biaya SPP: Rp", float, 1, 1_000_000_000)
    anak_karyawan = baca_ya_tidak("Anak karyawan? (y/n): ")
    ipk = baca_angka("IPK (0.0-4.0): ", float, 0.0, 4.0)
    tepat_waktu = baca_ya_tidak("Bayar tepat waktu? (y/n): ")

    utama, tambahan, kategori = hitung_diskon(ipk, anak_karyawan, tepat_waktu)
    total = utama + tambahan
    potongan = biaya * total
    final = biaya - potongan

    print("\n=== Hasil Perhitungan ===")
    print(f"Kategori utama  : {kategori} ({utama:.0%})")
    print(f"Diskon tepat waktu: {tambahan:.0%}")
    print(f"Total diskon    : {total:.0%}")
    print(f"Biaya SPP       : Rp{biaya:,.0f}")
    print(f"Potongan        : Rp{potongan:,.0f}")
    print(f"Biaya final     : Rp{final:,.0f}")


if __name__ == "__main__":
    main()
