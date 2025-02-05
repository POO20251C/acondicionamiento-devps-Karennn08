## Ejercicio 4: Invertir una Lista de Números
#Descripción: Dada una lista de números enteros separados por espacios, invierte el orden de los elementos y muestra la lista invertida en una sola línea.

def main():
    numbers = input('Space separated numbers: ')
    flippedNumbers = numbers[::-1]
    print('This is the flipped list: ',flippedNumbers)
main()