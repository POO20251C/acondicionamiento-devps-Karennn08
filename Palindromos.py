## Ejercicio 3: Verificar Palíndromo
##Descripción: Determina si una cadena de texto es un palíndromo, es decir, se lee igual de izquierda a derecha que de derecha a izquierda.  
#Importante: Debes ignorar espacios y diferencias entre mayúsculas y minúsculas.

def main():
    text = input('write something to find out if it is a palindrome: ')
    text = text.replace(" ", "").lower()
    flippedText = text[::-1].replace(" ", "").lower()

    if flippedText == text:
        print('Yes')
    else:
        print('Nop')
main()