#Tokenler üretmek 
import jwt 
import datetime

#Gizli anahtar
secret_key = "supersecretkey" 

#JWT oluşturma
token = jwt.encode(
    {"user_id": 123, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)},
    secret_key, 
    algorithm="HS256"
)
token= token if isinstance(token, str) else token.decode("utf-8")
print("Token:", token)

# JWT doğrulama
try:
    decoded = jwt.decode( token, secret_key, algorithms=["HS256"])
    print("Doğrulandı:",decoded)
except jwt.ExpiredSignatureError:
    print("Token süresi doldu.")
except jwt.InvalidTokenError:
    print("Geçersiz token.")