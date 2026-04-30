# ==========================================
# BAGIAN A: FUNGSI DAN LOGIKA PROGRAM
# ==========================================

def tentukan_pemenang(pilihan_user, pilihan_lawan):
    """Menentukan hasil pertandingan antara user dan lawan."""
    if pilihan_user == pilihan_lawan:
        return "Seri"
    elif (pilihan_user == "batu" and pilihan_lawan == "gunting") or \
         (pilihan_user == "kertas" and pilihan_lawan == "batu") or \
         (pilihan_user == "gunting" and pilihan_lawan == "kertas"):
        return "Menang"
    else:
        return "Kalah"

def mulai_permainan():
    """Fungsi utama untuk menjalankan loop permainan dan validasi input."""
    riwayat = []
    total_skor = 0
    
    while True:
        print("\n--- Ronde Baru ---")
        pilihan = input("Masukkan pilihan (batu/gunting/kertas) atau 'keluar': ").lower()
        
        if pilihan == "keluar":
            break
        
        # Validasi Input [cite: 8]
        if pilihan not in ["batu", "gunting", "kertas"]:
            print("Input tidak valid!")
            continue
            
        # Simulasi pilihan lawan (karena dilarang import, kita pakai pola sederhana)
        lawan = "batu" 
        hasil = tentukan_pemenang(pilihan, lawan) # Memanggil fungsi lain [cite: 8]
        
        if hasil == "Menang":
            total_skor += 10
            
        print(u"Hasil: " + hasil)
        # Menyimpan ke dalam list (untuk matriks 2D nanti) [cite: 8, 10]
        riwayat.append([len(riwayat) + 1, pilihan, hasil])
        
    return riwayat, total_skor

# ==========================================
# BAGIAN B: STRUKTUR DATA LIST DAN MATRIX 2D
# ==========================================

def tampilkan_riwayat(matriks_data):
    """Menampilkan riwayat pertandingan dalam format tabel."""
    if not matriks_data: # Penanganan list kosong [cite: 11]
        print("\nBelum ada riwayat pertandingan.")
        return

    print("\nRIWAYAT PERTANDINGAN")
    print("Ronde | Pilihan | Hasil")
    print("-" * 25)
    
    # Iterasi Matrix 2D 
    for baris in matriks_data:
        print(str(baris[0]) + "     | " + str(baris[1]) + "    | " + str(baris[2]))

# ==========================================
# BAGIAN C: ALGORITMA SORTING (BUBBLE SORT)
# ==========================================

def urutkan_leaderboard(data_skor):
    """Mengurutkan skor tertinggi menggunakan Bubble Sort (In-place copy)."""
    # Membuat salinan agar data asli tidak berubah 
    leaderboard = data_skor[:]
    
    n = len(leaderboard)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Membandingkan skor (elemen indeks ke-1)
            if leaderboard[j][1] < leaderboard[j + 1][1]:
                # Tukar posisi secara manual [cite: 13]
                leaderboard[j], leaderboard[j + 1] = leaderboard[j + 1], leaderboard[j]
                
    return leaderboard

# ==========================================
# ALUR DAN INTEGRASI PROGRAM UTAMA
# ==========================================

# Data dummy untuk leaderboard (Nama, Skor)
data_pemain = [["Budi", 50], ["Andi", 80], ["Caca", 30]]

# Jalankan Game
hasil_game, skor_akhir = mulai_permainan() # [cite: 17]

# Tambahkan skor user ke data pemain
data_pemain.append(["Anda", skor_akhir])

# Tampilkan Riwayat (Matriks 2D)
tampilkan_riwayat(hasil_game)

# Tampilkan Leaderboard (Sorting) 
print("\nLEADERBOARD (SKOR TERTINGGI)")
sorted_lb = urutkan_leaderboard(data_pemain)
for i in range(len(sorted_lb)):
    print(str(i+1) + ". " + sorted_lb[i][0] + " - " + str(sorted_lb[i][1]))