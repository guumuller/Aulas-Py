#exercício 2

"""
Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas
variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa. Mostrar o
conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.
"""

vA = int(input("Digite seu primeiro número:"))
vB = int(input("Digite seu segundo número:"))

print(vA, vB)

vA, vB = vB, vA

#aux = vB
#vB = vA
#vA = aux

print("Números invertidos:")
print(vA, vB)
