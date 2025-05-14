Öğrenci Not Takip Sistemi

Bu proje, öğrencilerin vize ve final notlarını kaydederek not ortalamalarını hesaplayan ve geçme/kalma durumlarını belirleyen bir not takip sistemi geliştirmeyi amaçlamaktadır. Python ile geliştirilen uygulama, kullanıcı dostu bir komut satırı arayüzü sunmakta ve öğrenci verilerini JSON formatında bir dosyada saklamaktadır. Modüler bir yapıda tasarlanan sistem; veri girişi, hata yönetimi ve dosya işlemleri gibi işlevleri ayrı modüller üzerinden gerçekleştirmektedir. Projeden beklenen temel çıktılar ise öğrenci ekleme, listeleme ve durum raporlama gibi temel işlevleri kapsamaktadır.

Projenin Amacı

Not takip sistemi, eğitim kurumlarında öğretmenlerin veya idari personelin öğrenci notlarını kolayca yönetmesi için geliştirilmiştir. Amaç, manuel not takibindeki hataları azaltmak, veri girişini kolaylaştırmak ve öğrenci performansını hızlıca değerlendirmektir. Proje şu problemleri çözmeyi hedefler: 
• Not girişinde geçersiz veri (Örn: 0-100 arasındaki notlar) sorununu önlemek.
• Öğrenci verilerini kalıcı olarak saklamak. 
• Kullanıcı dostu bir arayüz aracılığıyla hızlı ve verimli veri işleme sağlamak.

Özellikler

Öğrenci verilerini JSON formatında okur ve yazar
Notun 0-100 arasında olup olmadığını kontrol eder
Hatalı not girişlerinde özel bir hata (Exception) fırlatır
Öğrenci bilgisi ekleyebilir
Öğrenci bilgilerini tek bir liste halinde kullanıcıya sunar.
Dosyalar

dosya_islemleri.py: JSON veri işlemleri (yükleme ve kaydetme)
hata_yonetimi.py: NotAraligiHatasi adında özel bir hata sınıfı
veriler/ogrenciler.json: Öğrenci kayıtlarının tutulduğu dosya
Gereksinimler Python 3.7+

Standart kütüphaneler
