from abc import ABC, abstractmethod

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama=nama
        self.tahun=tahun_daftar
        self.saldo=saldo
        
    def lihat_saldo(self):
        print(f"Nama Akun : {self.nama}\nJumlah Saldo : Rp {self.saldo}")
        
    @abstractmethod
    def transfer_saldo(self):
        pass
    
    @abstractmethod
    def suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self):
        transfer=int(input("Masukkan Nominal Transfer : "))
        usia_akun=2023-self.tahun

        if self.saldo>=transfer:
            if transfer > 100000:
                if usia_akun >= 3:
                    self.saldo-=transfer
                    print("Berhasil transfer, biaya administrasi gratis\n")
                elif usia_akun < 3:
                    self.saldo-=transfer+2000
                    print("Berhasil transfer, biaya administrasi Rp 2000\n")
            else:
                self.saldo-=transfer
                print("Berhasil transfer, biaya administrasi gratis\n")
                
    def suku_bunga(self):
        usia_akun=2023-self.tahun
        
        if self.saldo>=1000000000:
            if usia_akun>=3:
                bunga=self.saldo*0.01
                print(f"Bunga bulanan akun {self.nama} sebesar Rp {bunga}\n")
            elif usia_akun<3:
                bunga=self.saldo*0.02
                print(f"Bunga bulanan akun {self.nama} sebesar Rp {bunga}\n")
        else:
            bunga=self.saldo*0.03
            print(f"Bunga bulanan akun {self.nama} sebesar Rp {bunga}\n")
            
class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self):
        transfer=int(input("Masukkan Nominal Transfer : "))
        usia_akun=2023-self.tahun
        if self.saldo>=transfer:
            if transfer > 100000:
                if usia_akun >= 3:
                    self.saldo-=transfer+2000
                    print("Berhasil transfer! biaya administrasi Rp 2000\n")
                elif usia_akun < 3:
                    self.saldo-=transfer+5000
                    print("Berhasil transfer! biaya administrasi Rp 5000\n")
            else:
                self.saldo-=transfer
                print("Berhasil transfer! biaya administrasi gratis\n")
                
    def suku_bunga(self):
        usia_akun=2023-self.tahun
        
        if self.saldo>=10000000:
            if usia_akun>=3:
                bunga=self.saldo*0.01
                print(f"Bunga bulanan akun {self.nama} sebesar Rp {bunga}\n")
            elif usia_akun<3:
                bunga=self.saldo*0.02
                print(f"Bunga bulanan akun {self.nama} sebesar Rp {bunga}\n")
        else:
            bunga=self.saldo*0.03
            print(f"Bunga bulanan akun {self.nama} sebesar Rp {bunga}\n")
            
akun1=AkunGold("Jeki", 2018, 2000000000)
akun2=AkunSilver("Kiya", 2022, 80000000)

akun1.lihat_saldo()
akun1.transfer_saldo()
akun1.lihat_saldo()
akun1.suku_bunga()

akun2.lihat_saldo()
akun2.transfer_saldo()
akun2.lihat_saldo()
akun2.suku_bunga()