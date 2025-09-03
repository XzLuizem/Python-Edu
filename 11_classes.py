### Classes ###

class MyEmptyPerson:
    pass


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y publicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.fullname = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.fullname} está caminando")


my_person = Person("Luis", "Michel")
print(my_person.fullname)
my_person.walk()

my_other_person = Person("Luis", "Michel", "XzLuizem")
print(my_other_person.fullname)
my_other_person.walk()
my_other_person.fullname = "Hector de León  (El loco de los perros)"
print(my_other_person.fullname)

my_other_person.fullname = 777
print(my_other_person.fullname)
