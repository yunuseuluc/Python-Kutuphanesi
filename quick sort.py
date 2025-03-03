#Listenin ortasında bir eleman seçerek o elemanın sağına büyükleri sola küçükleri atarak listeyi sıralıyor
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot= arr [len(arr) // 2]
    left= [x for x in arr if x < pivot]
    middle = [x for x in arr if x== pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr=[10, 6 ,54 ,0 ,-1 , 15, 869, -26, 42]
print(quick_sort(arr))
