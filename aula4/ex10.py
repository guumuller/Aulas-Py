# Exercício 10
"""
10. Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.
(nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
Cálculo da Média Ponderada = ------------------------------------------------------------------------
soma dos pesos
"""

nota1 = int(input("Nota 1: "))
pesoNota1 = int(input("Peso da Nota 1: "))
nota2 = int(input("Nota 2: "))
pesoNota2 = int(input("Peso da Nota 2: "))

mediaPonderada = (nota1 * pesoNota1) + (nota2 * pesoNota2)
print(mediaPonderada)