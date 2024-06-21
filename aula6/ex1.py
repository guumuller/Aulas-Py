"""
Exercício 1
Faça um algoritmo que leia dois números inteiros.
Se o primeiro número for menor que o segundo, imprima na tela todos os números inteiros entre eles. Caso não exista nenhum número inteiro entre eles imprima: "Não há números inteiros entre esses números".
Se os números forem iguais, imprima a mensagem: "Esses números são iguais."
Se o segundo número for maior que o primeiro, imprima todos os números entre o primeiro e o segundo de forma decremental.
"""

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))


if num1 < num2:
    for x in range(num1 + 1, num2, 1):
        print(x) 
if num1 == num2 -1 or num2 == num1 -1:
    print("Não há números inteiros entre esses números!")         
if num1 == num2:
    print("Esses números são iguais!")          
if num1 > num2:
    for x in range(num1 -1, num2, -1):    
        print(x)

"""
else:
    for x in range(num1, num2 + 1, -1):
        x = x -1
        print(x)
"""

        

   
