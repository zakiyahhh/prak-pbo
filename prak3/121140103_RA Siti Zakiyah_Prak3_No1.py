class AkunBank:
    list_pelanggan={}
    def __init__ (self, no, nama, saldo):
        self.__no_pelanggan = no
        self.__nama_pelanggan = nama
        self.__jumlah_saldo = saldo
        AkunBank.list_pelanggan.update({self.__no_pelanggan:self.__nama_pelanggan})
        self.menu=0

    def lihat_menu(self):
        print("Selamat datang di Bank Jago\n")
        print(self.__nama_pelanggan, ", ingin melakukan apa?")
        print("1. Lihat Saldo\n2. Tarik Tunai\n3. Transfer Saldo\n4. Keluar")
        self.menu=int(input("\nMasukkan nomor input : "))
        if self.menu == 1:
            self.lihat_saldo()
        elif self.menu == 2:
            self.tarik_tunai()
        elif self.menu == 3:
            self.transfer()
        else:
            print("\nTerimakasih, Sampai Jumpa!")

    def lihat_saldo(self):
        print(self.__nama_pelanggan, "memiliki saldo", self.__jumlah_saldo)

    def tarik_tunai(self):
        self.jumlah_tarik=int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if self.jumlah_tarik>self.__jumlah_saldo:
         print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo-=self.jumlah_tarik
            print("Saldo berhasil ditarik!")

    def transfer(self):
        self.jumlah_transfer=int(input("\nMasukkan nominal yang ingin ditranfer: "))
        if self.jumlah_transfer<=self.__jumlah_saldo:
            self.no_rek=int(input("Masukkan no rekening tujuan: "))
            if self.no_rek in self.list_pelanggan:
                print("Transfer Rp. ", self.jumlah_transfer, " ke ", self.no_rek, " sukses!")
                self.__jumlah_saldo-=self.jumlah_transfer

            else:
                print("No rekening tujuan tidak dikenal! Kembali ke menu utama...", )
        else:
            print("Nominal saldo yang anda punya tidak cukup!")

Akun1=AkunBank(1234, "Zakiyah", 5000000000)
Akun2=AkunBank(4321, "Ukraina", 6666666666)
Akun3=AkunBank(5678, "Elon Musk", 9999999999)

while Akun1.menu<4:
    Akun1.lihat_menu()
    print()
    print("Transaksi Selesai\n")
    
