# CONTAR PALABRAS 
def contar_ocurrencias(palabras):
    ocurrencias = {}
    for palabra in palabras:
        if palabra in ocurrencias:
            ocurrencias[palabra] += 1
        else:
            ocurrencias[palabra] = 1
    return ocurrencias
#2 DICCIONARIO
def combinar_diccionarios(dic1, dic2):
    resultado = dic1.copy()  
    for clave, valor in dic2.items():
        if clave in resultado:
            resultado[clave] += valor  
        else:
            resultado[clave] = valor  
    return resultado
  #3 FRECUENCIAS 
def contar_frecuencia(numeros):
    frecuencia = {}
    for numero in numeros:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 
    return frecuencia

#4 FILTRAR PALABRAS 
def filtrar_palabras_largas(palabras, longitud):
    palabras_largas = [palabra for palabra in palabras if len(palabra) > longitud]
    return palabras_largas

#5 INVERSION DE TUPLAS 
def invertir_tuplas(tuplas):
    tuplas_invertidas = [(b, a) for (a, b) in tuplas]
    return tuplas_invertidas
#6 ENCONTRAR EL VALOR MAS FRECUENTE 
def valor_mas_frecuente(numeros):
    frecuencia = {}
    for numero in numeros:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    max_frecuencia = max(frecuencia.values())
    for numero, cuenta in frecuencia.items():
        if cuenta == max_frecuencia:
            return numero
#7 SUBCONJUNTO
def es_subconjunto(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2):
conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}
resultado = es_subconjunto(conjunto1, conjunto2)
print(resultado)

# 8 AGRUPACION POR CLAVE 
def agrupar_por_edad(personas):
    agrupados = defaultdict(list)
    for persona in personas:
        nombre = persona["nombre"]
        edad = persona["edad"]
        agrupados[edad].append(nombre)
    return dict(agrupados)

# 9 UTILIZANDO LISTAS  
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)
def merge(izquierda, derecha):
    if not izquierda:
        return derecha
    if not derecha:
        return izquierda
    return [izquierda[0]] + merge(izquierda[1:], derecha) if izquierda[0] < derecha[0] else [derecha[0]] + merge(izquierda, derecha[1:])

# 10 ELIMINAR ELEMENTOS 
def eliminar_menores(lista, limite):
    return [x for x in lista if x >= limite]
numeros = [1, 2, 3, 4, 5]
limite = 3
resultado = eliminar_menores(numeros, limite)
print(resultado)

# 11 LIST OF LIST 
def aplanar_lista(lista_de_listas):
    return [item for sublista in lista_de_listas for item in sublista]
lista_de_listas = [[1, 2], [3, 4], [5]]
resultado = aplanar_lista(lista_de_listas)
print(resultado)

#12 CALCULO MEDIANA 
def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 1:
        return numeros_ordenados[n // 2]
    else:
        medio1 = numeros_ordenados[n // 2 - 1]
        medio2 = numeros_ordenados[n // 2]
        return (medio1 + medio2) / 2
    
# 13 DUPLICAR ELEMENTOS DE UNA LISTA 
def duplicar_elementos(lista):
   return [x for item in lista for x in (item, item)]
numeros = [1, 2, 3]
resultado = duplicar_elementos(numeros)
print(resultado)

 
# 14 CONTAR PALABRAS EN FRASES 
def contar_palabras(frases):
    conteo_palabras = {}
    for i in range(len(frases)):
        conteo_palabras[i] = len(frases[i].split())
    return conteo_palabras
frases = ["Yo creo que si", "tiene que contar", "las palabras"]
resultado = contar_palabras(frases)
print(resultado)

#15 CLAVE MAXIMA 
def clave_maxima(diccionario):
    return max(diccionario, key=diccionario.get)
diccionario = {'a': 10, 'b': 20, 'c': 5}
resultado = clave_maxima(diccionario)
print(resultado)

# 16 POLINDROMOS 
def encontrar_palindromos(palabras):
    return [palabra for palabra in palabras if palabra == palabra[::-1]]
palabras = ["oso", "otto", "tenet", "refer"]
resultado = encontrar_palindromos(palabras)
print(resultado)
