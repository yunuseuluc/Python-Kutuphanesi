#bir dizide veya listede belirli bir değeri aramaya yarayan bir algoritmadır
def linear_search(liste, aranan):
    for i in range (len(liste)):
        if liste[i] == aranan:
            return i
    return -1 

numaralar = [-3, 10, 23, 45, 70, 89, 5]
sonuc = linear_search(numaralar, 70)

if sonuc != -1:
    print(f"70 sayısı {sonuc}. indekste bulundu.")
else:
    print("70 sayısı listede bulunmadı.")    