### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Luis", "Michel", 36}
print(type(my_other_set))

print(len(my_other_set))  # Cantidad de elementos

# print(my_other_set[0])  # No se puede acceder por índice

my_other_set.add("XzLuizemDev")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("XzLuizemDev")  # Un set no admite elementos duplicados

print(my_other_set)

print("Michel" in my_other_set)  # Devuelve True si el elemento está en el set
# Devuelve False si el elemento no está en el set
print("Michal" in my_other_set)

my_other_set.remove("Michel")  # Elimina el elemento del set
print(my_other_set)

my_other_set.clear()  # Elimina todos los elementos del set
print(len(my_other_set))

del my_other_set  # Elimina la variable
# print(my_other_set)  # NameError: name 'my_other_set' is not defined

my_set = {"Luis", "Michel", 36}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(
    my_new_set.
    union(my_new_set).
    union(my_set).
    union({"JavaScript", "C#"})
)

# Elementos que están en my_new_set pero no en my_set
print(my_new_set.difference(my_set))
