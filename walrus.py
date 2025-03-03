# bir değeri atarken aynı zamanda o değeri döndürebilmek 
import walrus

while (user_input := input("Bir metin girin ( çıkmak için boş bırakın): ")) !="":
    print(f"Girdiğiniz metnin uzunluğu: {len(user_input)} karakter.)")