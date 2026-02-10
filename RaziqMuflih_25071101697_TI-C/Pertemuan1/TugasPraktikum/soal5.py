#definisi fungsi
def hitung(a,b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan,pengurangan

#memanggil fungsi
hasil_penjumlahan,hasil_pengurangan = hitung(5,3)

#menampilkan hasil
print('penjumlahan = ',hasil_penjumlahan)
print('pengurangan = ',hasil_pengurangan)