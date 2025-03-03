# hata mesajları daha net gösterebiliyoruz
from rich.traceback import install
install(show_locals=True)

def hata_olustur():
    return 1/0

hata_olustur()