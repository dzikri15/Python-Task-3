"""Soal Praktik 4 - Menu interaktif gabungan 3 studi kasus."""

IPK_MIN_AKTIF = 2.0
IPK_MIN_PERINGATAN = 1.5
SKS_MIN = 18
DISKON_ANAK_KARYAWAN = 0.25
DISKON_TEPAT_WAKTU = 0.05
BATAS_AMAN = 20
BATAS_PERINGATAN = 10


# ---------- helper input tervalidasi ----------
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


# ---------- logika bisnis ----------
def tentukan_status(ipk, sks, is_cuti):
    if is_cuti:
        return "Cuti"
    if ipk >= IPK_MIN_AKTIF and sks >= SKS_MIN:
        return "Aktif"
    if ipk >= IPK_MIN_PERINGATAN:
        return "Peringatan"
    return "Tidak Aktif"


def hitung_diskon(ipk, anak_karyawan, tepat_waktu):
    if anak_karyawan:
        utama, kategori = DISKON_ANAK_KARYAWAN, "Anak Karyawan"
    elif ipk >= 3.8:
        utama, kategori = 0.20, "Prestasi Tinggi"
    elif ipk >= 3.5:
        utama, kategori = 0.15, "Prestasi Baik"
    elif ipk >= 3.0:
        utama, kategori = 0.10, "IPK Memuaskan"
    else:
        utama, kategori = 0.0, "Tidak ada diskon utama"
    return utama + (DISKON_TEPAT_WAKTU if tepat_waktu else 0.0), kategori


def cek_status_stok(stok):
    if stok == 0:
        return "HABIS", "URGENT: restock segera!"
    if stok <= BATAS_PERINGATAN:
        return "RENDAH", "Restock dalam 1-3 hari"
    if stok <= BATAS_AMAN:
        return "PERINGATAN", "Rencanakan restock 1-2 minggu"
    return "AMAN", "Stok mencukupi"


# ---------- submenu ----------
def menu_status():
    print("\n[Cek Status Mahasiswa]")
    ipk = baca_angka("  IPK (0.0-4.0): ", float, 0.0, 4.0)
    sks = baca_angka("  SKS (0-24)   : ", int, 0, 24)
    cuti = baca_ya_tidak("  Sedang cuti? (y/n): ")
    print(f"  => Status: {tentukan_status(ipk, sks, cuti)}")


def menu_diskon():
    print("\n[Hitung Diskon Biaya]")
    biaya = baca_angka("  Biaya SPP: Rp", float, 1, 1_000_000_000)
    ak = baca_ya_tidak("  Anak karyawan? (y/n): ")
    ipk = baca_angka("  IPK (0.0-4.0): ", float, 0.0, 4.0)
    tw = baca_ya_tidak("  Bayar tepat waktu? (y/n): ")
    total, kategori = hitung_diskon(ipk, ak, tw)
    print(f"  Kategori : {kategori}")
    print(f"  Diskon   : {total:.0%}")
    print(f"  Potongan : Rp{biaya * total:,.0f}")
    print(f"  Bayar    : Rp{biaya * (1 - total):,.0f}")


def menu_stok():
    print("\n[Cek Peringatan Stok]")
    stok = baca_angka("  Jumlah stok: ", int, 0, 1_000_000)
    status, rek = cek_status_stok(stok)
    print(f"  => {status}: {rek}")


def main():
    print("=== Sistem Informasi Mahasiswa ===")
    while True:
        print("\nMenu:")
        print("1. Cek Status Mahasiswa")
        print("2. Hitung Diskon Biaya")
        print("3. Cek Peringatan Stok")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            menu_status()
        elif pilihan == "2":
            menu_diskon()
        elif pilihan == "3":
            menu_stok()
        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Pilih 1/2/3/0.")


if __name__ == "__main__":
    main()
