class Mhs:
    def __init__(self, nama, nim, kelas, sks):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks

    def Nama(self):
        print("Nama         : ", self.nama)
    def Nim(self):
        print("NIM          : ", self.nim)
    def Kelas(self):
        print("Kelas Siakad : ", self.kelas)
    def Sks(self):
        print("Jumlah SKS   : ", self.sks)

Mahasiswa = Mhs("RA Siti Zakiyah", 121140103, "PBO RB", 3)

Mahasiswa.Nama()
Mahasiswa.Nim()
Mahasiswa.Kelas()
Mahasiswa.Sks()
