#ifadeleri farklı desenlere göre kontrol ederek belirli desenlere uyan durumlarda kodu çalıştırma
status_code=404
match status_code:
    case 200:
        print("Başarılı")
    case 404:
        print("Bulunamadı!")
    case 500:
        print("Sunucu Hatası")
    case _:
        print("Bilinmeyen durum kodu.")
            