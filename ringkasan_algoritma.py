"""Soal Praktik 6 - Ringkasan algoritma dari 3 studi kasus."""

# ---------- aturan bisnis (sama dengan modul) ----------
def tentukan_status(mhs):
    if mhs["is_cuti"]:
        return "Cuti"
    if mhs["ipk"] >= 2.0 and mhs["sks"] >= 18:
        return "Aktif"
    if mhs["ipk"] >= 1.5:
        return "Peringatan"
    return "Tidak Aktif"


def hitung_diskon(ipk, anak_karyawan, tepat_waktu):
    if anak_karyawan:
        utama = 0.25
    elif ipk >= 3.8:
        utama = 0.20
    elif ipk >= 3.5:
        utama = 0.15
    elif ipk >= 3.0:
        utama = 0.10
    else:
        utama = 0.0
    return utama + (0.05 if tepat_waktu else 0.0)


def perlu_restock(stok):
    return stok <= 20  # PERINGATAN, RENDAH, HABIS


# ---------- data simulasi ----------
daftar_mhs = [
    {"nim": "2021001", "ipk": 3.52, "sks": 20, "is_cuti": False},
    {"nim": "2021002", "ipk": 1.75, "sks": 15, "is_cuti": False},
    {"nim": "2021003", "ipk": 3.90, "sks": 22, "is_cuti": False},
    {"nim": "2021004", "ipk": 1.20, "sks": 12, "is_cuti": False},
    {"nim": "2021005", "ipk": 3.00, "sks": 18, "is_cuti": True},
]
# (ipk, anak_karyawan, tepat_waktu)
kasus_diskon = [
    (3.9, False, True), (3.5, True, False),
    (2.8, False, True), (3.2, False, False),
]
stok_barang = [45, 12, 5, 0, 18, 30, 8, 0]


def main():
    # (a) persentase aktif vs tidak aktif
    total_mhs = len(daftar_mhs)
    jumlah_aktif = sum(1 for m in daftar_mhs if tentukan_status(m) == "Aktif")
    jumlah_tidak = total_mhs - jumlah_aktif
    persen_aktif = jumlah_aktif / total_mhs
    persen_tidak = jumlah_tidak / total_mhs

    # (b) rata-rata diskon
    daftar_diskon = [hitung_diskon(*k) for k in kasus_diskon]
    rata_diskon = sum(daftar_diskon) / len(daftar_diskon)

    # (c) persentase item perlu restock
    total_item = len(stok_barang)
    jumlah_restock = sum(1 for s in stok_barang if perlu_restock(s))
    persen_restock = jumlah_restock / total_item

    garis = "+" + "-" * 36 + "+" + "-" * 10 + "+" + "-" * 12 + "+"
    print(garis)
    print(f"| {'Ringkasan':<34} | {'Jumlah':>8} | {'Persentase':>10} |")
    print(garis)
    print(f"| {'Mahasiswa Aktif':<34} | {jumlah_aktif:>3}/{total_mhs:<4} | "
          f"{persen_aktif:>10.1%} |")
    print(f"| {'Tidak Aktif (selain Aktif)':<34} | "
          f"{jumlah_tidak:>3}/{total_mhs:<4} | {persen_tidak:>10.1%} |")
    print(f"| {'Rata-rata diskon diberikan':<34} | "
          f"{len(daftar_diskon):>3} kasus | {rata_diskon:>10.1%} |")
    print(f"| {'Item perlu restock':<34} | "
          f"{jumlah_restock:>3}/{total_item:<4} | {persen_restock:>10.1%} |")
    print(garis)


if __name__ == "__main__":
    main()
