## Ejercicio 1: Suma de Dígitos
##Descripción: Dado un número entero, calcula la suma de todos sus dígitos.
##Entrada:Una línea que contenga un número entero.
##Salida:Un entero que es la suma de los dígitos.

def main():
    numero = int(input("Numero al que desea sumarle los digitos: "))
    suma = 0
    while numero > 0:
        suma += numero%10
        numero //= 10
    print(suma)
main()
    