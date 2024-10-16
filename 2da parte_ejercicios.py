# VARIANTE 1 

# 1 Suma de dos numeros 
a = 10
b = 20
resultado = a + b
print(resultado)  

# 2 Concatenacion de cadenas 
cadena1 = "Hola"
cadena2 = "Mundo"
resultado = cadena1 + " " + cadena2
print(resultado)  # Debería mostrar "Hola Mundo"

# 3 Calcula el area de un rectangulo
base = 8
altura = 12
area = base * altura
print(area) 

# 4 Comprobar si un numero es par o impar 
num = 4
if num % 2 == 0:
    resultado = "Par"
else:
    resultado = "Impar"
print(resultado) 

# 5 Calcular el factorial de un numero 
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)  

# 6 Encontar el numero mas grande en una lista 
lista = [1, 2, 3, 4, 5]
numero_mas_grande = max(lista)
print(numero_mas_grande)  

# 7 Converti grados celsius 
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit) 

# 8 Verificar si el numero es primo 
num = 7
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
resultado = es_primo(num)
print(resultado)  

# 9 Contar cuentas veces aparece un  caracter en una cadena 
cadena = "programación"
caracter = "o"
contador = cadena.count(caracter)
print(contador) 

# 10  Sumar dos numeros en uhna lista 
lista = [1, 2, 3, 4, 5]
suma_total = sum(lista)
print(suma_total)  

# 11 Imprimir numeros pares en un rago 
inicio = 1
fin = 10
numeros_pares = []
for num in range(inicio, fin + 1):
    if num % 2 == 0:
        numeros_pares.append(num)
print(numeros_pares)  

# 12 Calcular el promedio de una lista de numeros 
lista = [1, 2, 3, 4, 5]
promedio = sum(lista) / len(lista)
print(promedio)  

# 13 Inverit una cadena 
cadena = "Python"
cadena_invertida = cadena[::-1]
print(cadena_invertida)  

# 14 Encontrar un  numero pequeno en una lista 
lista = [10, 20, 30, 40, 50]
numero_mas_pequeno = min(lista)
print(numero_mas_pequeno)  

# 15 Verificar si una palabra es polindromo 
palabra = "radar"
es_palindromo = palabra == palabra[::-1]
print(es_palindromo) 

# 16 Contar palabras en una horacion 
oracion = "Hola mundo"
contador_palabras = len(oracion.split())
print(contador_palabras) 

# 17 Calcular la potencia de un  numero 
base = 2
exponente = 3
resultado = base ** exponente
print(resultado)  

# 18 Calcular de kilomertos a millas 
kilometros = 5
millas = kilometros * 0.621371
print(millas)  

# 19 Crear una lista de numeros al cuadrado  
lista = [1, 2, 3, 4, 5]
lista_cuadrados = [num ** 2 for num in lista]
print(lista_cuadrados) 

# 20 Ordena una lista en orden asendente 
lista = [5, 3, 1, 4, 2]
lista_ordenada = sorted(lista)
print(lista_ordenada) 

# 21 contar los elementos de una lista 
lista = [1, 2, 3, 4, 5]
cantidad_elementos = len(lista)
print(cantidad_elementos)  

# 22 Encontrar la suma de dos digitos de un numero 
numero = 1234
suma_digitos = sum(int(digito) for digito in str(numero))
print(suma_digitos)  

# 23 Convertir una cadena a mayusculas 
cadena = "python"
cadena_mayusculas = cadena.upper()
print(cadena_mayusculas)  

# 24 Eliminar duplicado en una lista 
lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = list(set(lista))
lista_sin_duplicados.sort()
print(lista_sin_duplicados)   

# 25 Calcular el numero de vocales en una cadena 
cadena = "hola mundo"
vocales = "aeiou"
contador_vocales = sum(1 for letra in cadena if letra in vocales)
print(contador_vocales) 

# 26 Generar los primeros numeros de una cerie de fibonacci 
cadena = "hola mundo"
vocales = "aeiou"
contador_vocales = sum(1 for letra in cadena if letra in vocales)
print(contador_vocales)  

# 27 Eliminar los espacios en blanco de una cadena 
cadena = " hola mundo "
cadena_sin_espacios = cadena.replace(" ", "")
print(cadena_sin_espacios)  

# 28  Clalcula la cantidad de numeros impares 
inicio = 1
fin = 10
cantidad_impares = sum(1 for num in range(inicio, fin + 1) if num % 2 != 0)
print(cantidad_impares)  

# 29 Crear un diccionario con claves invertidas y valores ivertidos 
diccionario = {"a": 1, "b": 2, "c": 3}
diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}
print(diccionario_invertido)  

# 30 Calcula la longuitud de una lista 
lista = [1, 2, 3, 4, 5]
longitud_lista = len(lista)
print(longitud_lista)  

# 31 Suma las claves de unn diccionaio 
diccionario = {1: "a", 2: "b", 3: "c"}
suma_claves = sum(diccionario.keys())
print(suma_claves)

# 32 Convertir una lista de cadenas a mayusculas 
lista = ["python", "java", "c++"]
lista_mayusculas = [cadena.upper() for cadena in lista]
print(lista_mayusculas)
  
