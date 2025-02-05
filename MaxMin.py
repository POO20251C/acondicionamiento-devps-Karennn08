## Ejercicio 6: Encontrar el Máximo y Mínimo
#Descripción: Dada una lista de números enteros separados por espacios, determina cuál es el número mayor y cuál es el menor.

def main():
    text = input('Write a list of numbers to find out max and min: ')
    numbers = text.split() #default space separator
    print('El maximo es:', max(numbers), 'y el minimo es:', min(numbers))
main()