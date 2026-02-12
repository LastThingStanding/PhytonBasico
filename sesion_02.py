# Tuplas
mi_tupla= (2,4)
print("mi tupla: ",mi_tupla)

# Lista
mi_lista = {1, 3.1416,"christian",mi_tupla}
print("El primer elemento de mi lista",mi_lista[0])
print("El cuarto elemento de mi lista",mi_lista[3])
print("el tercer elemento de mi lista",mi_lista[2])

# Diccionarios
mi_diccionario ={"mi_lista": mi_lista,
                 "Nombre":"christian",
                 "Pi":3.1416,
                 "Tel":664-7978827}
print("Llave para accesar a mi direccion mi_lista",mi_diccionario["mi_lista"])
print("Llave para accesar a mi direccion Pi",mi_diccionario["Pi"])
print("Llave para accesar a mi direccion Tel",mi_diccionario["Tel"])
