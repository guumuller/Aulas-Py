# Exercício 1
# Faça um algoritmo que leia uma frase e diga quantas 
# vogais existem na frase digitada.(considerar apenas AaEeIiOoUu)

frase = input("Digite uma frase: ")

vogais = 0

for caracter in frase:
    if caracter in "AaEeIiOoUu":
        vogais += 1

print("Quantidade de vogais: ", vogais)

'''
for caracter in frase:
    if caracter == "A" or caracter == "a":
        vogais += 1;
    if caracter == "E" or caracter == "e":
        vogais += 1;
    if caracter == "I" or caracter == "i":
        vogais += 1;
    if caracter == "O" or caracter == "o":
        vogais += 1;
    if caracter == "U" or caracter == "u":
        vogais += 1;

print("Quantidade de vogais: ", vogais)
'''