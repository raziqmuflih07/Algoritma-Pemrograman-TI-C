class Sendal:
    def __init__(self, merk, harga,size):
        self.merk= merk
        self.harga= harga
        self.size= size

    def membeli_sendal(self):
        print(f"saya membeli sendal dengan merk{self.merk}","dengan harga {self.harga}","dan ukurannya adalah {self.size}")

    def merk_baru(self,merk_baru):
        self.merk = merk_baru
        print(f"saya membeli sendal lain dengan merk {merk_baru}")

sendalSatu= Sendal("eiger",100000,42)
sendalDua= Sendal("adidas",50000,40)
sendalTiga= Sendal("jepit",10000,41)

print(sendalSatu.merk)
print(sendalSatu.harga)
print(sendalSatu.size)
sendalSatu.merk_baru("swallow")


