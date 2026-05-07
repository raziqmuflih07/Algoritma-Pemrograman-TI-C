import os

folder_script = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder_script)

def list_files():
    files = [f for f in os.listdir('.') if f.endswith('.txt')]
    if not files:
        print("tidak ada file .txt ditemukan.")
        return None
    
    print("\n file tersedia: ")
    for i,f in enumerate(files, 1):
        print(f"[{i}] {f}")
    return files

def read():
    files = list_files()
    if not files:
        return
    
    try:
        index= int(input("pilih file (nomor): ")) - 1
        file = files[index]

        print(f"\n--- isi {file} ---")
        with open (file, "r") as f:
            print(f.read())
            print("-" * 25)
    except (ValueError,IndexError):
        print("Error: input nomor tidak valid.")
    except Exception as e:
        print(f"gagal membaca file: {e}")



def write():
    files = list_files()
    user_input = input("\npilih file (nomor) atau ketik nama file baru: ")
    file= ""
    try:
        index = int(user_input) - 1
        file = files[index]
    except (ValueError, IndexError, TypeError):
        file = user_input
        if not file.endswith('.txt'):
            file += '.txt'

    isi = input("masukkan isi teks:\n")

    try:
        with open (file, "w")as f:
            f.write(isi)
        print("file berhasil disimpan")
    except Exception as e:
        print(f"gagal menulis file: {e}")



def delete():
    files = list_files()
    if not files:
        return
    try:
        index = int(input("pilih file (nomor): "))-1
        file = files[index]

        konfirmasi = input(f"apakah anda yakin ingin menghapus '{file}' ? (y/n): ")
        if konfirmasi == 'y':
            if os.path.exists(file):
                os.remove(file)
                print("file berhasil dihapus.")
        else:
            print("penghapusan dibatalkan")

    except(ValueError, IndexError):
        print("error: input nomor tidak valid.")
    except Exception as e:
        print(f"gagal menghapus file: {e}")



def main():
    while True:
        print("=" * 30 + "\n")
        print("PYTHON FILE MANAGER v1.0\n")
        print("=" * 30 + "\n")

        print("[1] Read file")
        print("[2] Write file")
        print("[3] Delete file")
        print("[0] Exit")
        print("=" * 30 + "\n")

        pilihan= input("pilih menu: ")

        if pilihan == '1':
            read()
        elif pilihan == '2':
            write()
        elif pilihan == '3':
            delete()
        elif pilihan == '0':
            break
        else:
            print("pilihan tidak valid")


if __name__ == "__main__":
    main()

