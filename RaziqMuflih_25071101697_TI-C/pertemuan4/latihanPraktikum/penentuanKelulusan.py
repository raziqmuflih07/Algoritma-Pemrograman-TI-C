print ("=====program penentu kelulusan=====")

try:
    ipk = float(input("masukkan ipk mahasiswa : "))


    if ipk <= 2.5:
        print("status : tidak lulus")
    elif ipk > 4.0:
        print("ipk tidak valid")
    elif ipk < 0:
        print("ipk tidak valid")
    else :
        print("status : anda lulus")

except ValueError :
    print ("hanya boleh memasukkan angka")

finally:
    print("program berhasil")