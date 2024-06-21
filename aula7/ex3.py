# Exercício 3
# Faça um algoritmo que leia um texto e diga quantas 
# palavras existem neste texto.

texto = input("Digite um texto:")

texto_separado = texto.split()
palavra = 0

for i in texto_separado:
     palavra += 1
        
print("Quantidade de letras: ", palavra)