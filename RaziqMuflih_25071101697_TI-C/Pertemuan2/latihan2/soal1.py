def rata_rata(nilai):
    if len (nilai) == 0:
        return "maaf, data kosong"
    
    TotalNilai = sum(nilai)
    JumlahNilai = len(nilai)
    hasil = TotalNilai / JumlahNilai
    return hasil

nilaiMahasiswa = [80,75,90,60,85]
output = rata_rata(nilaiMahasiswa)

print (f'nilai rata-rata dari seorang mahasiswa itu adalah =', output)