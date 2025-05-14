from ogrenci import Ogrenci
from dosya_islemleri import ogrencileri_yukle, ogrencileri_kaydet
from hata_yonetimi import NotAraligiHatasi

def not_girisi(etiket):
    try:
        not_degeri = float(input(f"{etiket} notunu giriniz: "))
        if not 0 <= not_degeri <= 100:
            raise NotAraligiHatasi()
        return not_degeri
    except ValueError:
        print("Geçersiz giriş. Sayı giriniz.")
        return not_girisi(etiket)
    except NotAraligiHatasi as e:
        print(e)
        return not_girisi(etiket)

def ogrenci_ekle():
    ad = input("Ogrencinin adı: ")
    soyad = input("Öğrencinin soyadı: ")
    vize = not_girisi("Vize")
    final = not_girisi("Final")
    yeni = Ogrenci(ad, soyad, vize, final)
    

    ortalama = (vize * 0.4) + (final * 0.6)
    yeni.ortalama = ortalama

  
    if final < 30:
        durum = "Kaldı (Final notu 30'dan düşük)"
    elif ortalama >= 60:
        durum = "Geçti"
    else:
        durum = "Kaldı (Ortalama 60'dan düşük)"

    print("Öğrenci Başarıyla Oluşturuldu.")
    print(f"{yeni.ad} {yeni.soyad} - Vize: {vize}, Final: {final}, Ortalama: {ortalama}, Durum: {durum}")

    # Öğrenci verilerini dosyaya kaydet
    veriler = ogrencileri_yukle()
    veriler.append({
        "ad": yeni.ad,
        "soyad": yeni.soyad,
        "vize": yeni.vize,
        "final": yeni.final,
        "ortalama": yeni.ortalama,
        "durum": durum
    })
    ogrencileri_kaydet(veriler)

def ogrencileri_goster():
    veriler = ogrencileri_yukle()
    if not veriler:
        print("Kayıtlı öğrenci yok.")
        return
    for i, ogr in enumerate(veriler, 1):
        print(f"{i}. {ogr['ad']} {ogr['soyad']} - Ortalama: {ogr['ortalama']}, Durum: {ogr['durum']}")

def menu():
    while True:
        print("\n1. Öğrencileri Ekle\n2. Öğrencileri Listele\n3. Cikis")
        secim = input("Seçiminiz: ")

        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrencileri_goster()
        elif secim == "3":
            break
        else:
            print("Geçersiz seçim")

if __name__ == "__main__":
    menu()
