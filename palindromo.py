import unicodedata
import string

phrase = input("Digite a frase: ").upper()

#Usa a normalização NFD (Separa os caracteres)
phrase_normalize = unicodedata.normalize("NFD", phrase)
print(phrase)

# Remove os acentos (caracteres com categoria "Mn")

phrase_without_diacritics = ''.join(c for c in phrase_normalize 
                                    if unicodedata.category(c) != 'Mn')

print(phrase_without_diacritics)

# Remove pontuações

phrase_without_punctuation = ''.join(c for c in phrase_without_diacritics if c not in string.punctuation)

print(phrase_without_punctuation)

# Remove os espaços 
phrase_without_space = phrase_without_punctuation.replace(' ','')
print(phrase_without_space)

# Criação da lista/lista inversa
lista = [c for c in phrase_without_space]
print(lista)

lista_reverse = lista[::-1]
print(lista_reverse)

#Compara as duas listas para verificar se é palíndromo

if lista == lista_reverse: 
    print("Essa frase é palíndromo")
else: 
    print("Essa frase não é palíndromo")


#------------------------------------------------------------------------------------------------------

import unicodedata

def eh_palindromo(phrase):
    phrase = str(phrase.upper())
    phrase  = unicodedata.normalize("NFD", phrase)
    phrase = ''.join(c for c in phrase if unicodedata.category(c) != 'Mn')
    phrase = ''.join(c for c in phrase if c not in string.punctuation)
    phrase = phrase.replace(' ','')
    return phrase == phrase[::-1]


while True:
    phrase_verification = input("Digite a palvara ou frase para a verificação: ")

    if eh_palindromo(phrase_verification):
        print("Esse nome é palíndromo")
    else:
        print("Isso não é um palíndromo")

