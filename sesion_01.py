# Numeros
print(int(7))
print(float(7.7))
print(type(7))
print(float(10 % 3))
print(float(25 % 4))
print(float(16 % 2))
print(float(10 / 3))
print(float(10 / 3))

# variables
print("============VARIABLE==============")
x = 100
y = 1
print(x + y)

ventas = 1999991
print("Nuestras ventas fueron:", ventas)

is_active = True
print(is_active)

game_over = False
print(game_over)

some_string = "Hola soy un string"
print(some_string)

print("============CONDICIONALES==============")

edad = 15
if edad >= 18:
    print("Si puedes entrar al bar")
else:
    print("No puedes entrar al bar")

mi_numero = int(input("¿Cuál es el número que deseas verificar?: "))
print(f"El número que desea verificar es {mi_numero}")

if mi_numero % 2 == 0:
    print(f"El número {mi_numero} es par")
else:
    print(f"El número {mi_numero} es impar")


def par_impar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")


print("============FUNCION PAR_IMPAR==============")

mi_numero = int(input("¿Cuál es el número que deseas verificar?: "))
print(f"El número que desea verificar es {mi_numero}")
par_impar(mi_numero)
