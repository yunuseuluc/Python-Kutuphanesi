#kelimeleri karşılaştırmak ve benzerlik oran için hesaplanır
from fuzzywuzzy import fuzz

oran = fuzz.ratio("apple", "apell")
print(f"Benzerlik oranı: {oran}" )