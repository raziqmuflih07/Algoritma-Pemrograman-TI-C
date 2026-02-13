class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis

    def sound(self):
        return "suara"
    
class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.__merk = merk
        self.tahun_rilis = tahun_rilis

    def get_merk(self):
        return self.__merk

class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis):
        self.__jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis

    def get_jenis(self):
        return self.__jenis
    
V1 = Vehicle("kapal", "titanic", 1967)
print(V1.sound())
V2 = Mobil("listrik","Xiaomi","2022")
print(V2.get_merk())
V3 = Motor("bensin","revo","2011")
print(V3.get_jenis())
