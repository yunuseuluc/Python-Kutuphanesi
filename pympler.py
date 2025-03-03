#hafıza yönetimi ve optimizasyon için geliştirilmiş
from pympler import asizeof

obj = [i for i in range (15)]
print(asizeof.asizeof(obj))
