# . (nokta): Tek bir karakteri temsil eder.
# ^ (Başlangıç): Dizgenin başlangıcını temsil eder.
# $ (Bitiş): Dizgenin sonunu temsil eder.
# * (yıldız): Önceki karakterin sıfır veya daha fazla tekrarını temsil eder.
# + (artı): Önceki karakterin bir veya daha fazla tekrarını temsil eder.
# [] (Köşeli Parantez): Belirtilen karakterlerden birini temsil eder.

""""""
import re

text = "Python metin"

mathches = re.findall(r"^Python", text)

if mathches:
    print("Metin 'python' kelimesiyle başlıyor..")
else:
    print("Metin 'python' kelimesiyle başlamıyor..")