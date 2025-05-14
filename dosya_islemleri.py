import json
import os

def veri_yolu():
    return "veriler/ogrenciler.json"

def ogrencileri_yukle():
    if not os.path.exists(veri_yolu()):
        return []
    with open(veri_yolu(), "r", encoding="utf-8") as f:
        return json.load(f)

def ogrencileri_kaydet(ogrenci_listesi):
    with open(veri_yolu(), "w", encoding="utf-8") as f:
        json.dump(ogrenci_listesi, f, indent=2, ensure_ascii=False)
