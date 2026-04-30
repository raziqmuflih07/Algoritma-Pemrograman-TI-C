struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

#TUGAS A --> HITUNG TOTAL UKURAN
def total_ukuran(folder: dict) -> int:
    total =0
    for nilai in folder.values():
        if isinstance(nilai,dict):
            total+= total_ukuran(nilai)
        else:
            total+= nilai
    return total


#TUGAS B -->HITUNG JUMLAH FILE
def hitung_file(folder: dict) -> int:
    total = 0
    for nilai in folder.values():
        if isinstance(nilai,dict):
            total += hitung_file(nilai)
        else:
            total += 1
    return total

#TUGAS C --> CARI FILE TERBESAR
def cari_terbesar(folder: dict) -> tuple:
    file_terbesar = ""
    ukuran_terbesar = 0

    for nama, nilai in folder.items():
        if isinstance(nilai, dict):
            nama_file, ukuran_file = cari_terbesar(nilai)

            if ukuran_file > ukuran_terbesar:
                ukuran_terbesar = ukuran_file
                file_terbesar = nama_file

        else:
            if nilai > ukuran_terbesar:
                ukuran_terbesar = nilai
                file_terbesar = nama

    return file_terbesar,ukuran_terbesar

#TUGAS D --> CETAK STRUKTUR FOLDER
def tampilkan_tree(folder: dict, nama: str = "root", level: int =0):
    indentasi = "   "* level

    print(f"{indentasi}📂 {nama}")

    for key,nilai in folder.items():
        if isinstance(nilai,dict):
            tampilkan_tree(nilai, key, level + 1)
        else:
            indentasi_file = "  " * (level + 1)
            print(f"{indentasi_file} 📄 {key} ({nilai} KB)")

tampilkan_tree(struktur)

hasil_total_kb = total_ukuran(struktur)
print(f"\nTotal ukuran skripsi : {hasil_total_kb} KB")

total_file = hitung_file(struktur)
print(f"Jumlah file : {total_file} file")

file_besar,ukuran_besar = cari_terbesar(struktur)
print(f"file terbesar: {file_besar} ({ukuran_besar} KB)")
