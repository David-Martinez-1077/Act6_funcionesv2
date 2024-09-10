print("Más sobre funciones")
#Aquí se escriben las funciones
def suma_ab(a, b):
    s = a + b
    return s
def resta_ab(num1,num2):
    resultado = num1 - num2
    return resultado
def multiplicacion_ab(num1, num2):
    resultado = num1 * num2;
    return resultado
def division_ab(num1, num2):
    resultado = num1 / num2
    return resultado

# llamadas a funciones
print("Calculando suma")
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
suma = suma_ab(n1, n2)
print(f"La suma de {n1} + {n2} es: {suma}\n")

print("Calculando resta")
resta1 = int(input("Escribe el primer número a restar: "))
resta2 = int(input("Escribe el segundo número a restar: "))
resta = resta_ab(resta1, resta2)
print(f"La resta de {resta1} - {resta2} es: {resta}\n")

print("Calculando multiplicación")
multiplicacion1 = int(input("Escribe el primer número a multiplicar: "))
multiplicacion2 = int(input("Escribe el segundo número a multiplicar: "))
multiplicacion = multiplicacion_ab(multiplicacion1, multiplicacion2)
print(f"La multiplicación de {multiplicacion1} * {multiplicacion2} es: {multiplicacion}\n")

print("Calculando división")
division1 = int(input("Escribe el primer número a dividir: "))
division12 = int(input("Escribe el segundo número a dividir: "))
division = division_ab(division1, division12)
print(f"La división de {division1} / {division12} es: {division}")








