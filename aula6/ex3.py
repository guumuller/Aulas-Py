"""
Exercício 3
Altere o exercício anterior para que a digitação dos números aceite somente números positivos
"""
for r in range(3):
    num1 = 0
    while num1 <= 0:
        num1 = int(input("Digite o primeiro número:"))
        if num1 <= 0:
            print("Número inválido! Digite novamente.") 
    while True:
        num2 = int(input("Digite o segundo número:"))
        if num2 <= 0:
            print("Número inválido! Digite novamente.")
        else:
            break
    
    if num1 < num2:
        for x in range(num1 + 1, num2, 1):
            print(x) 
    elif num1 == num2 -1 or num2 == num1 -1:
        print("Não há números inteiros entre esses números!")         
    elif num1 == num2:
        print("Esses números são iguais!")          
    if num1 > num2:
        for x in range(num1 -1, num2, -1):    
            print(x)

