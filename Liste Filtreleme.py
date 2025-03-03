# sayı listesi 
sayilar = [1,2,3,4,5,6,7,8,9,10]

# Filtreleme

cift_sayilar = [sayi1 for sayi1 in sayilar if sayi1 % 2 == 0 ]

print("Orjinal liste:", sayilar)
print("Filtrelenmiş çift sayılar", cift_sayilar)