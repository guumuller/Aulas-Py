"""
Exercício 2
Altere o exercício anterior para que a digitação dos números aconteça 3 vezes.
"""
for r in range(3):
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
