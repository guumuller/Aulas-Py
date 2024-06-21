#Exercício 11
"""
11. Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus
Centígrados.
(Fahrenheit – 32) x 5/9
Fórmula: Centígrados = ----------------------------
"""

graus = int(input("Graus (Fahrenheit): "))

conversao = (graus - 32) * 5/9
print(conversao)