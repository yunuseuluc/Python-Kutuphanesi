#instagramdaki profıl fotosunu çekiyor 
import instaloader

ig = instaloader.Instaloader()
dp = input("Kullanıcı Adını gir: ")

ig.download_profile(dp, profile_pic_only=True)