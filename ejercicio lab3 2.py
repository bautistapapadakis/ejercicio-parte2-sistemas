# Definir función
def sumar(a, b):
    resultado = a + b
    return resultado

# Capturar valores del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Llamar a la función
res = sumar(num1, num2)

# Mostrar resultado
print("La suma es:", res)