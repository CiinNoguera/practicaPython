"""
EL FAMOSO "FIZZ BUZZ":
Escribe un programa que muestre por consola (con un print) los números 
de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresión),
sustituyendo los siguiente:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizz_buzz():
    for i in  range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0 :
            print("buzz")
        else:
            print(i)

fizz_buzz()

"""
¿ES UN ANAGRAMA?
Escribe un programa que diga si una palabra es una anagrama de otra.
Que retorne un bool que indique si es o no un anagrama. 
"""

def anagrama():
    palabra1 = input("Igresa una palabra")
    palabra2 = input("Ingresa otra palabra")

    if sorted(palabra1) == sorted(palabra2):
        print("Es un anagrama")
        return True
    else:
        print("No es un anagrama")
        return False
anagrama()  

def palindromo():
    palabra1 = input("Ingrese una palabra")
    palabra2 = input("Ingrese la segunda palabra")

    if palabra1 == palabra2[::-1]:
        print("Es un palíndromo")
    else:
        print("Las palabras ingresadas no son un palíndromo")

palindromo()  

"""
SUCESIÓN DE FIBONACCI

Escribe un programa que improma los 50 primeros números de la sucesión 
de Fibonacci empezando por cero. 
-La sucesión de Fibonacci se compone por una sucesión de números
 en la que el siguiente siempre es la suma de los dos anteriores.

"""

def fibonacci():
#     a = 0
#     b = 1
#     for i in range(50):
#         print(a)
#         a, b = b, a + b
        
# fibonacci()


    n_prev = 0
    n_next = 1

    for i in range(0, 50):
        print(n_prev)
        fib = n_prev + n_next
        n_prev = n_next
        n_next = fib

fibonacci()       

"""
NÚMEROS PRIMOS
Escribe un programa que se encargue de comprobar si un número es o no primo.
- Imprime los números primos del 1 al 100

"""

def n_primo():

    for number in range(1, 101):
        if number >= 2:

            is_divisible = False

            for i in range(2, number):
                if number % i == 0:
                    is_divisible = True
                    break
        
        if not is_divisible:
            print(number)
    
    n_primo()
    

    """
    Crea un programa que invierta el orden de una cadena de texto
    sin usar funciones propias del lenguaje que lo hagan de forma automática.
    
    """

    def reverse(text):
        reverse_text = ""
        for char in text:
            reverse_text = char + reverse_text

        return reverse_text
    print(reverse("Hola Mundo"))