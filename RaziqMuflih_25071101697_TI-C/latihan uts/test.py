#==================
#bagian 1
#==================
def hitung_status(nilai):
    """menentukan status keluusan mahasiswa"""
    if nilai >= 60:
        return "lulus"
    else:
        return "gagal"
    
def input_data():
    """mengambil input data mahasiswa dan nilai secara berulang"""
    data_mahasiswa = []

    while True:
        nama = input("masukkan nama mahasiswa (ketik 'selesai' untuk mengakhiri ): ").upper()

        if nama == "SELESAI":
            break 

        try:
            nilai = int(input("masukkan nilai mahasiswa (0-100) : "))
            if nilai < 0 or nilai > 100:
                print("error!!!!Nilai tidak valid,harap masukkan nomor yang valid!!")
                continue
        except ValueError:
            print("Error : harap masukkan angka untuk nilai!!")
            continue

        status = hitung_status(nilai)

        data_mahasiswa.append([nama,nilai,status])
    
    return data_mahasiswa

#=====================
#bagian 2
#=====================

def cetak_tabel(data_matriks):
    """menampilkan data mahasiswa dalam bentuk tabel"""
    if not data_matriks:
        print("\ndata mahasiswa masih kosong")
        return
    
    print("\n" + "=" * 30)
    print("Nama           |Nilai   |Status")
    print("=" * 30)

    for i in range(len(data_matriks)):
        mhs = data_matriks[i]

        no = str(i+1) + ". "
        nama_mhs= str(mhs[0]).ljust(12)
        nilai_mhs = str(mhs[1]).ljust(7)
        status_mhs = str(mhs[2])
        print(no + nama_mhs + "|" + nilai_mhs + "|" + status_mhs)


#======================
#bagian 3
#======================

def urutkan_nilai(data_matriks):
    """mengurutkan nama mahasiswa berdasarkan nilai tertinggi"""
    ranking = data_matriks[:]

    n = len(ranking)
    for i in range(n):
        for j in range(n-i-1):
            if ranking[j][1] < ranking[j+1][1]:
                ranking[j],ranking[j+1] = ranking[j+1],ranking[j]
    
    return ranking

#==================
#Alur dan integrasi
#==================

data_mhs = input_data()

print("\ndata mahasiswa sesuai input: ")
cetak_tabel(data_mhs)

print("\nranking mahasiswa : ")
ranking_mhs = urutkan_nilai(data_mhs)

if ranking_mhs:
    for i in range(len(ranking_mhs)):
        rank = str(i+1) + ". "
        nama = ranking_mhs[i][0]
        nilai = str(ranking_mhs[i][1])
        print(rank + nama + "(" + nilai + ")")