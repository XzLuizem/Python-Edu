### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (36, 1.74, "Luis", "Michel", "Luis")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) # IndexError
# print(my_tuple[-6]) # IndexError

# Devuelve la cantidad de veces que aparece el valor
print(my_tuple.count("Luis"))
print(my_tuple.index("Michel"))  # Devuelve la posición del valor
# Devuelve la posición de la primera aparición del valor
print(my_tuple.index("Luis"))

# my_tuple[1] = 1.80 # TypeError: 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "XzLuizemDev"
my_tuple.insert(1, "Celeste")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2]  # TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple)  # NameError: name 'my_tuple' is not defined
