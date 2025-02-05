## Ejercicio 2: Contar Vocales en una Cadena
##Descripción: Dada una cadena de texto, cuenta el número de vocales 
#(a, e, i, o, u, sin distinguir mayúsculas de minúsculas) que contiene.

def countVowels(word, vowels):
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count

def main():
    vowels = ('a', 'e', 'i', 'o', 'u' )
    word = input("Write a word to count its vocals: ") #hay que practicar ingles jejeje
    numberVowels = countVowels(word.lower(), vowels)
    print(numberVowels)
main()