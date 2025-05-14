class Ogrenci:
    def __init__(self, ad, soyad, vize, final):
        self.ad = ad
        self.soyad = soyad
        self.vize = vize
        self.final = final
        self.ortalama = self.ortalama_hesapla()
        self.durum = self.durum_belirle()

    def ortalama_hesapla(self):
        return round((self.vize * 0.4 + self.final * 0.6), 2)

    def durum_belirle(self):
        if self.final < 30:
            return "Kaldı (Final notu 30'dan düşük)"
        elif self.ortalama >= 60:
            return "Geçti"
        else:
            return "Kaldı (Ortalama 60'dan düşük)"

    def __str__(self):
        return f"{self.ad} {self.soyad} - Vize: {self.vize}, Final: {self.final}, Ortalama: {self.ortalama}, Durum: {self.durum}"
