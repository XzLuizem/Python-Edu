### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Luis",
                 "Apellido": "Michel", "Edad": 36, 1: "Python"}

my_dict = {
    "Nombre": "Luis",
    "Apellido": "Michel",
    "Edad": 36,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.74
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
print(my_dict["Apellido"])
print(my_dict["Edad"])
print(my_dict["Lenguajes"])
print(my_dict[1])

my_dict["Nombre"] = "Juan"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Programadores"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Luis" in my_dict)  # Busca la clave "Luis" = False
print("Apellido" in my_dict)  # Busca la clave "Apellido" = True

print(my_dict.items())  # Devuelve una lista de tuplas
print(my_dict.keys())  # Devuelve una lista de claves
print(my_dict.values())  # Devuelve una lista de valores

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
# Crea un nuevo diccionario con claves de my_dict y valor None
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "XzLuizemDev")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict))  # Convierte las claves del diccionario en una lista
print(tuple(my_new_dict))  # Convierte las claves del diccionario en una tupla
print(set(my_new_dict))  # Convierte las claves del diccionario en un conjunto


# Crea un nuevo diccionario con claves de my_list y valor "Vacío"
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"), "Vacío")
print(my_new_dict)
