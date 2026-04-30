#==================
#BAGIAN A
#==================
DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"] 

riwayat =[]

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    """menentukan pemenangnya berdasarkan pilihan"""
    if (pilihan_pemain == "gunting" and pilihan_komputer == "batu" or
        pilihan_pemain == "batu" and pilihan_komputer == "kertas" or
        pilihan_pemain == "kertas" and pilihan_komputer =="gunting"):
        return "komputer menang"
    elif (pilihan_pemain == pilihan_komputer):
        return "seri"
    else:
       return "pemain menang"
    
def main_satu_giliran(nomor_giliran):
    """memasukkan input dari pemain """
    komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)] 
    pemain =input(["masukkan pilihan anda(hanya menerima batu/gunting/kertas) : "]).lower()
    seri =[]

    if pemain not in DAFTAR_PILIHAN:
            print("pilihan tidak valid,harap masukkan pilihan yg sesuai!!!")

    return pemain,komputer,seri

def main_satu_ronde(nama, nomor_ronde):
    """menghitung dan menentukan pemenang dari permainan"""
    no_giliran = 0
    menang_pemain= 0
    menang_komputer = 0 


    while menang_pemain < 3 or menang_komputer < 3:
        hasil = main_satu_giliran(no_giliran)
        no_giliran +=1
        if hasil == "pemain":
            menang_pemain +=1
        if hasil == "komputer":
            menang_komputer +=1

    return no_giliran,menang_pemain,menang_komputer

#==================
#BAGIAN B
#==================

def tampilkan_riwayat(riwayat):
    """menampilkan riwayat dari satu ronde"""
    riwayat = main_satu_ronde[:]
    if not riwayat:
        print("belum ada riwayat")

    print("\n=" *27 )
    print("Nomor     |Nama      |skor")
    print("=" *27)

    for i in riwayat:
        nomor = str[riwayat[i][0]].ljust(9)
        nama = str[riwayat[i][1]].ljust(9)
        skor = str[riwayat[i][2]].ljust(6)
        print(nomor + "|" + nama + "|" + skor + "|")

#==================
#BAGIAN C
#==================

def bubble_sort_riwayat(riwayat):
    """menampilkan salinan dari riwayat"""
    pass

