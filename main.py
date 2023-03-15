#ESTRUCTURA SELECTIVA Y REPETITIVA
#Una estructura selectiva es una estructura de control de flujo que permite al programa tomar decisiones
#basadas en una condición o expresión lógica. En Python, las estructuras selectivas se implementan a través
#de las palabras clave if, else, elif (contracción de "else if") y switch.
## una estructura selectiva permite que el programa tome decisiones y ejecute diferentes bloques
# de código en función de una condición determinada.

#Estructuras selectivas
edad = 20

if edad >= 18:
    print("Eres mayor de edad")

#Estructuras repetitivas
numero = 1

while numero <= 10:
    print(numero)
    numero += 1

#CONVERSION DE TIPOS DE DATOS
#Para convertir un string a un entero o a un float, se utiliza la función int() o la función float(),
# respectivamente Si el string no puede ser convertido a un número, se producirá un error de tipo ValueError.
#Conversión de string a int o float
numero_entero = int("10")
numero_float = float("3.14")

#conversión de int o float a string Para convertir un número a un string, se utiliza la función str().

numero_entero = 10
numero_float = 3.14

texto_entero = str(numero_entero)
texto_float = str(numero_float)

#Conversión de string a boolean
#Para convertir un string a un boolean, se utiliza la función bool(). En Python, los siguientes valores
# son considerados False: False, None, 0, 0.0, "" (string vacío), [] (lista vacía), () (tupla vacía) y {}
# (diccionario vacío). Cualquier otro valor se considera True.

valor_booleano = bool("True")  # True

#Conversión de boolean a int
#Para convertir un boolean a un entero, se utiliza la
#función int(). En Python, True se convierte a 1 y False se convierte a 0.

valor_entero = int(True)  # 1

#Conversión de int a float y viceversa
numero_entero = 10
numero_float = 3.14

numero_float_desde_entero = float(numero_entero)
numero_entero_desde_float = int(numero_float)

#LISTAS
#En Python, una lista es una estructura de datos que permite almacenar un conjunto de valores en una
#única variable. Los elementos de una lista pueden ser de cualquier tipo de datos y pueden ser accedidos
#ejemplo
familiares = ["Juan", "María", "Pedro", "Ana", "Luisa"]
amigos = ["Carlos", "Marta", "Pablo", "Lucía"]
conocidos = ["Roberto", "Fernanda", "Javier"]
nombres = ["Juan", "María", "Pedro", "Ana", "Luisa"]

# Imprimir todos los elementos de la lista
print(nombres)

# Imprimir un elemento de la lista
print(nombres[2])

# Imprimir varios elementos de la lista utilizando slicing
print(nombres[1:4])

#TUPLAS
#es una colección ordenada e inmutable de elementos, que pueden ser de diferentes tipos de datos
#(cadenas de texto, números, booleanos, etc.).  A diferencia de las listas, las tuplas no se pueden modificar una vez creadas.

# Ejemplo
tupla1 = ("caballo", "gato", "pato")

# Imprimir la tupla completa
print(tupla1)

# Imprimir un elemento de la tupla
print(tupla1[1])

# Imprimir varios elementos de la tupla
print(tupla1[0:2])

#DICCIONARIOS
#es una estructura de datos que permite almacenar una colección de elementos, donde cada elemento se compone de una clave y un valor.
#Cada clave debe ser única dentro del diccionario, mientras que el valor puede ser cualquier tipo de objeto de
# Python, como un número, una cadena de texto, una lista, otra estructura de datos, e incluso otro diccionario.
# Ejemplo 1
frutas = {"papas": 2, "chocorramo": 3, "bombom": 1}

# Ejemplo 2
persona = {"nombre": "Paola", "edad": 20, "ciudad": "Popayan"}

# Ejemplo 3
vacio = {} # diccionario vacío
