lst_nome = []
lst_idade = []
lst_genero = []

soma_idades = 0
pessoa_mais_velha = ''
idade_mais_velha = 0
total_feminino = 0

while True:
    nome = input("Digite seu nome ou 'fim' para encerrar: ")
    if nome == 'fim':
        break
    else:
        lst_nome.append(nome)        
    idade = int(input("Digite sua idade: "))
    lst_idade.append(idade)
    genero = input ("Digite seu gênero: ")
    while genero not in ['F', 'M']:
        genero = input("Gênero inválido. Digite novamente (F/M): ")


lst_genero.append(genero)
        
soma_idades += idade
#if idade > idade_mais_velha:
#   idade_mais_velha = idade

idade_mais_velha = max(lst_idade)

if idade_mais_velha in lst_idade:
    posicao = lst_idade.index(idade_mais_velha)
    
    
if genero == 'F':
    total_feminino += 1

media_idades = soma_idades / len(lst_idade)

percentual_feminino = (total_feminino / len(lst_genero)) * 100


print("\nMédia de idades:", media_idades)
print(f"{lst_nome[posicao]} é a pessoa mais velha. ")
print("Percentual de pessoas do gênero Feminino:", percentual_feminino, "%") 