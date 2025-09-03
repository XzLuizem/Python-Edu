### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))  # Cantidad de elementos

my_other_list = [35, 1.74, "Luis", "Michel"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))  # Cuenta cuántas veces aparece el valor
# print(my_other_list[4])  # IndexError
# print(my_other_list[-5])  # IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = (
    my_other_list[2],
    my_other_list[1],
    my_other_list[0],
    my_other_list[3]
)
print(age)

print(my_list + my_other_list)
# print(my_list - my_other_list) # TypeError

# Agrega "XzLuizemDev" al final de la lista
my_other_list.append("XzLuizemDev")
print(my_other_list)

my_other_list.insert(1, "Celeste")  # Inserta "Celeste" en la posición 1
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove("Rojo")  # Elimina la primera aparición del valor
print(my_other_list)

my_list.remove(30)  # Elimina la primera aparición del valor
print(my_list)

print(my_list.pop())  # Elimina el último elemento
print(my_list)

my_pop_element = my_list.pop(2)  # Guarda el elemento eliminado en una variable
print(my_pop_element)
print(my_list)

del my_list[2]  # Elimina el elemento en la posición 2
print(my_list)

my_new_list = my_list.copy()  # Crea una copia de la lista

my_list.clear()  # Elimina todos los elementos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()  # Invierte el orden de los elementos
print(my_new_list)

my_new_list.sort()  # Ordena los elementos de menor a mayor
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list))
