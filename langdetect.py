#Dilleri algılıyor
from langdetect import detect

text="[도깨비 OST Part 1] 찬열, 펀치 "
detect_language = detect(text)
print(f"Algılanan dil: {detect_language}" )