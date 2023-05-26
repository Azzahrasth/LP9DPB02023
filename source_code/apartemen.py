from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, tower,lantai, jml_penghuni, jml_kamar):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.tower = tower
        self.lantai = lantai

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_tower(self):
        return self.tower
    
    def get_lantai(self):
        return self.lantai
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nTower : " + str(self.tower) +"\nLantai : " + str(self.lantai) +"\nJumlah Kamar : " + str(self.jml_kamar) + "\nJumlah Orang : " + str(self.jml_penghuni) + "\n"