"""
Para o exercício considere as seguintes listas: 
listaA, listaB, listaC
Você tem um código funcional mas parcial que mostra
um menu com várias opções. 
Você deverá finalizar o código implementando 
as opções que faltam.
"""
menu = """
    ========================================
    1- Adicionar um elemento na listaA
    2- Retirar um elemento na listaA
    3- Digite um número e mostre sua posição 
        na listaA
    4- Digite uma posição e diga qual o número 
        ocupa essa posição na listaA
    5- Copie todos os números para pares da 
        listaA para a listaB
    6- Copie da listaA para a listaC todos os 
        números que tiverem apenas 2 dígitos
    7- Imprima todas as listas mostrando o 
        nome da lista, seus elementos e suas posições.
    8- Finaliza o código
    ========================================    """

listaA = []
listaB = []
listaC = []

while True:
    print(menu)
    escolha = input("Escolha: ")
    if escolha == '1':
        numero = int(input("Digite um número: "))
        listaA.append(numero)
        
    if escolha == '2':
        
        # remove - remove o elemento da lista.
        
        print(listaA)
        numero = int(input("Que número deseja retirar? "))
        if numero in listaA:
            listaA.remove(numero)
        else:
            print("Este número não está na lista!!")
        print(listaA)
        
        
        # pop - remove o elemento pelo indice.
        """
        indice = int(input("Digite a posição para retirar elemento: "))
        if indice >= 0 and indice < len(listaA):
            listaA.pop(indice)
        else:
            print("Este indice não pertence a lista!!")
        print(listaA)
        """
        
    if escolha == '3':
        print(listaA)
        numero = int(input("Digite um número da lista: "))
        if numero in listaA:
            posicao = listaA.index(numero)
            print(posicao)
        else:
            print("O número não está na lista!!")
        pass
        

    if escolha == '4':
        print(listaA)
        indice = int(input("Digite um indice da lista: "))
        numero = listaA[indice]
        print(numero)
        
    if escolha == '5':
        listaB = [numero for numero in listaA if numero % 2 == 0]
        print(listaB)
        
    if escolha == '6':
        for numero in listaA:
            if 10 <= numero <=99:
                listaC.append(numero)
    print(listaC)
    
    if escolha == '7':
        # seu código aqui
        pass
    if escolha == '8':
        break