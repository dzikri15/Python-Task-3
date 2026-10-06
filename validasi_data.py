"""Soal Praktik 5 - Validasi data mahasiswa (mengembalikan list error)."""


def validasi_mahasiswa(nim, ipk, sks, semester):
    """Terima input mentah (string), kembalikan list pesan error.
    List kosong berarti semua data valid."""
    errors = []

    # NIM: 10 digit angka, tahun 2000-2037
    nim = str(nim).strip()
    if len(nim) != 10:
        errors.append("NIM harus 10 karakter")
    elif not nim.isdigit():
        errors.append("NIM harus berisi angka saja")
    elif not 2000 <= int(nim[:4]) <= 2037:
        errors.append("Tahun masuk pada NIM harus 2000-2037")

    # IPK: 0.0 - 4.0
    try:
        if not 0.0 <= float(ipk) <= 4.0:
            errors.append("IPK harus antara 0.0 dan 4.0")
    except ValueError:
        errors.append("IPK harus berupa angka")

    # SKS: 0 - 24 (bilangan bulat)
    try:
        if not 0 <= int(sks) <= 24:
            errors.append("SKS harus antara 0 dan 24")
    except ValueError:
        errors.append("SKS harus berupa bilangan bulat")

    # Semester: 1 - 14 (bilangan bulat)
    try:
        if not 1 <= int(semester) <= 14:
            errors.append("Semester harus antara 1 dan 14")
    except ValueError:
        errors.append("Semester harus berupa bilangan bulat")

    return errors


def main():
    print("=== Validasi Data Mahasiswa ===")
    nim = input("NIM      : ")
    ipk = input("IPK      : ")
    sks = input("SKS      : ")
    semester = input("Semester : ")

    errors = validasi_mahasiswa(nim, ipk, sks, semester)
    print("\n=== Hasil Validasi ===")
    if not errors:
        print("Semua data VALID.")
    else:
        print(f"Ditemukan {len(errors)} kesalahan:")
        for no, pesan in enumerate(errors, start=1):
            print(f"  {no}. {pesan}")


if __name__ == "__main__":
    main()
