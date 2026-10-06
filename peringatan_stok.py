"""Soal Praktik 3 - Sistem peringatan stok (8 item, semua level)."""

BATAS_AMAN = 20
BATAS_PERINGATAN = 10

inventaris = [
    {"kode": "B001", "nama": "Buku Python",     "stok": 45, "harga": 85000},
    {"kode": "B002", "nama": "Buku Database",   "stok": 12, "harga": 95000},
    {"kode": "B003", "nama": "Flashdisk 16GB",  "stok": 5,  "harga": 50000},
    {"kode": "B004", "nama": "Kabel USB",       "stok": 0,  "harga": 25000},
    {"kode": "B005", "nama": "Mouse Wireless",  "stok": 18, "harga": 120000},
    {"kode": "B006", "nama": "Keyboard",        "stok": 30, "harga": 150000},
    {"kode": "B007", "nama": "Headset",         "stok": 8,  "harga": 175000},
    {"kode": "B008", "nama": "Webcam HD",       "stok": 0,  "harga": 220000},
]


def cek_status_stok(stok):
    """Return (status, rekomendasi, prioritas)."""
    if stok == 0:
        return "HABIS", "URGENT: restock segera!", "CRITICAL"
    if stok <= BATAS_PERINGATAN:
        return "RENDAH", "Restock dalam 1-3 hari", "HIGH"
    if stok <= BATAS_AMAN:
        return "PERINGATAN", "Rencanakan restock 1-2 minggu", "MEDIUM"
    return "AMAN", "Stok mencukupi", "LOW"


def main():
    print("=" * 72)
    print("LAPORAN STATUS INVENTARIS")
    print("=" * 72)
    print(f"{'Kode':<6} {'Nama':<16} {'Stok':>4} {'Nilai (Rp)':>13}  "
          f"{'Status':<11} Prioritas")
    print("-" * 72)

    total_nilai = 0
    hitung = {"AMAN": 0, "PERINGATAN": 0, "RENDAH": 0, "HABIS": 0}
    perlu_tindakan = []

    for item in inventaris:
        status, rekomendasi, prioritas = cek_status_stok(item["stok"])
        nilai = item["stok"] * item["harga"]
        total_nilai += nilai
        hitung[status] += 1
        if prioritas != "LOW":
            perlu_tindakan.append((item, rekomendasi, prioritas))
        print(f"{item['kode']:<6} {item['nama']:<16} {item['stok']:>4} "
              f"{nilai:>13,}  {status:<11} {prioritas}")

    total_item = len(inventaris)
    print("\n--- Rekomendasi Tindakan ---")
    urutan = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2}
    for item, rek, prio in sorted(perlu_tindakan, key=lambda t: urutan[t[2]]):
        print(f"[{prio:<8}] {item['nama']:<16} -> {rek}")

    print("\n--- Ringkasan Statistik ---")
    print(f"Total item            : {total_item}")
    for status, jumlah in hitung.items():
        print(f"  {status:<11}: {jumlah} item ({jumlah / total_item:.0%})")
    print(f"Item perlu tindakan   : {len(perlu_tindakan)} dari {total_item}")
    print(f"Total nilai inventaris: Rp{total_nilai:,}")
    print(f"Rata-rata stok/item   : "
          f"{sum(i['stok'] for i in inventaris) / total_item:.1f} unit")


if __name__ == "__main__":
    main()
