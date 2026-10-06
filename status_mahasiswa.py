"""Soal Praktik 1 - Laporan status 5 mahasiswa."""

IPK_MIN_AKTIF = 2.0
IPK_MIN_PERINGATAN = 1.5
SKS_MIN = 18
JUMLAH_MAHASISWA = 5


def baca_angka(prompt, tipe, minimum, maksimum):
    """Ulangi input sampai valid (tipe benar dan dalam rentang)."""
    while True:
        try:
            nilai = tipe(input(prompt))
        except ValueError:
            print("  Error: masukkan angka yang valid")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Error: nilai harus antara {minimum} dan {maksimum}")


def baca_teks(prompt):
    while True:
        teks = input(prompt).strip()
        if teks:
            return teks
        print("  Error: tidak boleh kosong")


def tentukan_status(ipk, sks):
    if ipk >= IPK_MIN_AKTIF and sks >= SKS_MIN:
        return "Aktif"
    if ipk >= IPK_MIN_PERINGATAN:
        return "Peringatan"
    return "Tidak Aktif"


def main():
    daftar = []
    for i in range(1, JUMLAH_MAHASISWA + 1):
        print(f"\n--- Mahasiswa {i} dari {JUMLAH_MAHASISWA} ---")
        nim = baca_teks("NIM  : ")
        nama = baca_teks("Nama : ")
        ipk = baca_angka("IPK (0.0-4.0) : ", float, 0.0, 4.0)
        sks = baca_angka("SKS (0-24)    : ", int, 0, 24)
        daftar.append({"nim": nim, "nama": nama, "ipk": ipk, "sks": sks})

    print("\n" + "=" * 62)
    print("LAPORAN STATUS MAHASISWA")
    print("=" * 62)
    print(f"{'NIM':<12} {'Nama':<16} {'IPK':>5} {'SKS':>4}  Status")
    print("-" * 62)
    for mhs in daftar:
        status = tentukan_status(mhs["ipk"], mhs["sks"])
        print(f"{mhs['nim']:<12} {mhs['nama']:<16} {mhs['ipk']:>5.2f} "
              f"{mhs['sks']:>4}  {status}")


if __name__ == "__main__":
    main()
