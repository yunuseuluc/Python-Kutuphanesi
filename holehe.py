#Yazdığımız e postanın hangi sitelerde kayıtlı olup olmadığını öğrenebiliyoruz
import subprocess

def mail_kontrolet(email):
    result = subprocess.run(["holehe", email], capture_output=True, text=True)
    return result.stdout

email = "ninja.yunus72@hotmail.com"
response = mail_kontrolet(email)
print(response)

