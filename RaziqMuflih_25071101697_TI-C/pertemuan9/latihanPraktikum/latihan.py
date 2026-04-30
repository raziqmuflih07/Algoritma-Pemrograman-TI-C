import copy

# ==========================================
# Implementasi Algoritma Pengurutan
# ==========================================

def insertion_sort(arr):
    """Mengurutkan array dengan memindahkan elemen ke posisi yang tepat satu per satu."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    """Mengurutkan array menggunakan strategi divide and conquer dengan pivot."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def counting_sort(arr):
    """Mengurutkan array berdasarkan frekuensi kemunculan angka (efektif untuk non-negatif)."""
    if not arr:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    # Menghitung frekuensi
    for num in arr:
        count[num] += 1
    
    # Menyusun kembali array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

# ==========================================
# Fungsi Utility & Validasi
# ==========================================

def get_valid_input(prompt):
    """Memastikan input pengguna adalah bilangan bulat non-negatif."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Kesalahan: Harap masukkan bilangan bulat non-negatif (>= 0).")
                continue
            return value
        except ValueError:
            print("Kesalahan: Input harus berupa angka bulat.")

def main():
    print("=== Program Pengurutan Array (Struktur Data) ===")
    
    n = get_valid_input("Masukkan jumlah elemen array: ")
    
    original_array = []
    for i in range(n):
        element = get_valid_input(f"Masukkan elemen ke-{i+1}: ")
        original_array.append(element)
    
    print("\n" + "="*40)
    print(f"Array Asli: {original_array}")
    print("="*40 + "\n")

    # --- Eksekusi Insertion Sort ---
    print("1. [INSERTION SORT]")
    arr_ins = copy.deepcopy(original_array)
    print(f"Sebelum: {arr_ins}")
    hasil_ins = insertion_sort(arr_ins)
    print(f"Sesudah: {hasil_ins}\n")

    # --- Eksekusi Quick Sort ---
    print("2. [QUICK SORT]")
    arr_quick = copy.deepcopy(original_array)
    print(f"Sebelum: {arr_quick}")
    hasil_quick = quick_sort(arr_quick)
    print(f"Sesudah: {hasil_quick}\n")

    # --- Eksekusi Counting Sort ---
    print("3. [COUNTING SORT]")
    arr_count = copy.deepcopy(original_array)
    print(f"Sebelum: {arr_count}")
    hasil_count = counting_sort(arr_count)
    print(f"Sesudah: {hasil_count}\n")

if __name__ == "__main__":
    main()