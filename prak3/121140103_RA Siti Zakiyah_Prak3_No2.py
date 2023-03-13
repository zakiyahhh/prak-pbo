class Mahasiswa:
    #atribut class
    semester=4
    
    def __init__(self, nama, nim):
        #atribut public
        self.nama = nama
        self.nim = nim
        #atribut protected
        self._ipk = 0
        #atribut private
        self.__status_mhs = False
    
    #fungsi mencetak status mahasiswa aktif
    def status_mhs(self):
        self.__status_mhs = True
        print("Mahasiswa Aktif")
    
    #fungsi mencetak status mahasiswa tidak aktif   
    def statuss_mhs(self):
        self.__status_mhs = False
        print("Mahasiswa Tidak Aktif")
    
    #mengupdate nilai ipk
    def _update_ipk(self, nilai):
        self._ipk += nilai
    
    def besar_ipk(self, nilai):
        if self.__status_mhs:
            self._update_ipk(nilai)
            print(f"{self.nama} {self.nim} besar ipk : {nilai}")
        else:
            print("coba ulangi")
    
    #fungsi mencetak nilai ipk        
    def get_ipk(self):
        return self._ipk
        

Bio1 = Mahasiswa("Zakiyah", "121140103")
print(f"Nama     : {Bio1.nama}")
print(f"NIM      : {Bio1.nim}")
print(f"Semester : {Bio1.semester} \n")

Bio1.status_mhs()
Bio1.besar_ipk(3.9)
print(f"Besar ipk : {Bio1.get_ipk()}")