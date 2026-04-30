buku = [["algoritma",2000],
        ["basis data",2500],
        ["kalkulus",3000],
        ["statistik",3500],
        ["logmat",4000]
        ]

j=0
for i in buku:
    if j < 6:
        j += 1
    print(f"{j}.{i}")


noBuku=input("masukkan nomor buku= ")
if noBuku in buku:
    print(buku)
else:
    print("error!!!,nomor tidak ada")