#exercício 3

"""
Ler dois valores numéricos e escrever a soma destes.
"""

def soma_dois_numeros(num1, num2):
  soma = num1 + num2
  return soma

num1 = int(input("Número 1:"))
num2 = int(input("Número 2:"))

soma = soma_dois_numeros(num1, num2)

#  OU  soma = num1 + num2
# print(soma)  OU 
print(soma_dois_numeros(num1, num2))
