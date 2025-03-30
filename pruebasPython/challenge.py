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