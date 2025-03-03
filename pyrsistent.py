from pyrsistent import pvector

#Değişmez bir liste 
immutable_list = pvector([1, 2, 3])
print("Orijinal liste:", immutable_list)

#yeni bir öge eklerken orjinal listeyi değişmez
new_list = immutable_list.append(4)
print("Yeni liste:", new_list)
print("Orjinal liste (değişmedi):", immutable_list)

#immutable yapılarla hata yapma riski azalır