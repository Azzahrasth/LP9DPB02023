from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik,jml_lantai, jml_penghuni, jml_kamar):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.jml_lantai = jml_lantai

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_jml_lantai(self):
        return self.jml_lantai
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Lantai : " + str(self.jml_lantai) +"\nJumlah Kamar : " + str(self.jml_kamar) + "\nJumlah Orang : " + str(self.jml_penghuni) + "\n"
   