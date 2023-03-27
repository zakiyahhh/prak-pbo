#RA Siti Zakiyah
#121140103


class Komputer:

  def __init__(self, nama, jenis, harga, merek):
    self.nama = nama
    self.jenis = jenis
    self.harga = harga
    self.merek = merek

class Processor(Komputer):

  def __init__(self, nama, jenis, harga, merek, jumlah, kecepatan):
    super().__init__(nama, jenis, harga, merek)
    self.jumlah_core = jumlah
    self.kecepatan_processor = kecepatan

  def tampil(self):
    print(f"Processor {self.nama} produksi {self.merek}")

class RAM(Komputer):

  def __init__(self, nama, jenis, harga, merek, kapasitas):
    super().__init__(nama, jenis, harga, merek)
    self.kapasitas = kapasitas

  def tampil(self):
    print(f"Processor {self.nama} produksi {self.merek}")

class HDD(Komputer):

  def __init__(self, nama, jenis, harga, merek, kapasitas, rpm):
    super().__init__(nama, jenis, harga, merek)
    self.kapasitas = kapasitas
    self.rpm = rpm

  def tampil(self):
    print(f"Processor {self.nama} produksi {self.merek}")

class VGA(Komputer):

  def __init__(self, nama, jenis, harga, merek, kapasitas):
    super().__init__(nama, jenis, harga, merek)
    self.kapasitas = kapasitas

  def tampil(self):
    print(f"Processor {self.nama} produksi {self.merek}")

class PSU(Komputer):
  def __init__(self, nama, jenis, harga, merek, daya):
    super().__init__(nama, jenis, harga, merek)
    self.daya = daya

  def tampil(self):
    print(f"Processor {self.nama} produksi {self.merek}")

rakit = []

p1 = Processor('Core i7 7740X', 'Baru', 4350000, 'Intel', 4, '4.3GHz')
p2 = Processor('Ryzen 5 3600', 'Baru', 250000, 'AMD', 4, '4.3GHz')
ram1 = RAM('DDR4 SODimm PC19200/2400MHz', 'Baru', 328000, 'V-Gen', '4GB')
ram2 = RAM('DDR4 2400MHz', 'Baru', 328000, 'G.SKILL', '4GB')
hdd1 = HDD('HDD 2.5 inch', 'Baru', 295000, 'Seagate', '500GB', 7200)
hdd2 = HDD('HDD 2.5 inch', 'Baru', 295000, 'Seagate', '1000GB', 7200)
vga1 = VGA('VGA GTX 1050', 'Baru', 250000, 'Asus', '2GB')
vga2 = VGA('1060Ti', 'Baru', 250000, 'Asus', '8GB')
psu1 = PSU('Corsair V550', 'Baru', 250000, 'Corsair', '500W')
psu2 = PSU('Corsair V550', 'Baru', 250000, 'Corsair', '500W')

rakit.extend([[p1, ram1, hdd1, vga1, psu1], [p2, ram2, hdd2, vga2, psu2]])

for x in range(len(rakit)):
  print("Komputer", x + 1, ":")
  for y in range(len(rakit[x])):
    rakit[x][y].tampil()
  print()
