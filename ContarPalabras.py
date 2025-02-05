## Ejercicio 5: Contar Palabras en una Cadena
#Descripción: Dada una cadena de texto, cuenta la cantidad de palabras que contiene. Se asume que las palabras están separadas por uno o más espacios.

def main():
    text = input('Write somthig to count the words: ')
    words = text.split() #default space separator
    print('There are', len(words), 'words')
main()