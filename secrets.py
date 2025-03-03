#güvenli ve rastgele veri üretir özellikle parola ve API keyler
import secrets

token = secrets.token_hex(16)
print(token)