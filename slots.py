#bir sınıfın yalnızca belirli öz niteliklere sahip olmasına yarıyor bu sayede hafıza kullanımını azaltıyor
#ve performansı arttırıyor
class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Obje oluşturma
p = Point(x=10, y=20)
