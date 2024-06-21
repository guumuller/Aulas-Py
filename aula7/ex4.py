# Exercício 4
# Faça um algoritmo que leia uma string no formato de data (dd/mm/aaaa)
# e escreva esta com o nome do mês por extenso.
#Exemplo: 
#entrada: 10/04/2024
#saida : 10 de abril de 2024.

data = input("Digite uma data (d/mm/aaaa): ")
dia = data[:2]
mes = data[3:5]
ano = data[6:]
meses = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",]
i_mes = int(mes)
mes_extenso = meses[i_mes]
print(f"{dia} de {mes_extenso} de {ano}")