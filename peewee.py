# SQL kullanmadan veri tabanı ile etkileşim halinde oluyor
from peewee import *

db = SqliteDatabase('yunus_example.db')

# Tabloyu temsil eden model sınıfı
class User(Model):
    name= CharField()
    age= IntegerField()

    class Meta:
        database = db

db.connect()
db. create_tables([User])

user= User.create(name="yunus", age="24")

#Kullanıcıyı göster
for user in User.select():
    print(user.name, user.age)
