#Klavye ve fare girişleri izlemek ve kontrol etmek,kullanıcı etkileşiminide simüle etmek için
from pynput import keyboard

def on_press(key):
    print(F"{key} tuşuna basıldı.")

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
