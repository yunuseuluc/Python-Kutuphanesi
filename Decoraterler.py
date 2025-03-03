#fonksiyonların yada metotların davranışlarını değiştirmek veya genişlettirmek için kullanılan özel bir yapı
def Sevgilim(fn):
    def inner():
        fn()
        print("Nasılsın iyimisin") 
        print("Kendine iyi bak")
    return inner

@Sevgilim
def günaydın():
    print("Günaydınnnnn ")

günaydın()    