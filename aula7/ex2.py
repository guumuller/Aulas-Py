# Exercício 2
# Faça um algoritmo que leia um texto com até 20 caracteres, 
# e imprima esse texto de traz para frente.
"""
texto = input("Digite um texto: ")
if len(texto) <= 20:
    for ind in range(len(texto)-1, -1, -1):
        print(texto[ind], end="")
else:
    print("O texto possui mais de 20 letras!")
    



while True:
    texto = input("Digite um texto: ") 
    tam = len(texto)  
    if  tam > 20:       
        print("O texto possui mais de 20 letras!")
        continue
    else:
        break



print(texto [::-1])
"""

while True:
    texto = input("Digite ym texto (max. 20 caracteres): ")
    if len(texto) >= 20:
        input(f"Máximo 20 caracteres.")
    else:
        break

print("Imprimindo texto invertido")
print(texto[::-1])
