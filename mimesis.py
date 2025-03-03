#Sahte veriler üretiyor
from mimesis import Person
person=Person('tr')
print(person.full_name())
print(person.email())