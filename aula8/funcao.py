#Reescrita ex1 aula7

"""
def nome_da_funcao():
    print("Estou dentro da função.")

nome_da_funcao()

input("???")
"""
"""
def contar_vogais(frase):
    qt = 0
    vogais = "aeiou"
    for caracter in frase:
        if caracter in vogais:
            qt += 1
    return qt

def ler_frase():
    return input("Digite uma frase: ")

frase_digitada = ler_frase()
qt_vogais = contar_vogais(frase_digitada)
print(f"A quantidade de vogais na frase é: {qt_vogais}.")
"""
"""
#Reescrita ex2 aula 7
def ler_texto():
    while True:
        texto = input("Digite ym texto (max. 20 caracteres): ")
        if len(texto) >= 20:
            input(f"Máximo 20 caracteres")
        else: return texto
        
def imprimir_texto(texto):
    print("Imprimindo texto invertido:")
    print(texto_ok[::-1])
    
texto_ok = ler_texto()
imprimir_texto(texto_ok)
"""
#Reescrita ex3 aula 7
def ler_texto():
    return input("Digite um texto: ")

def converter_em_lista(texto):
    return texto.split()

def contar_palavras(lista):
    return len(lista)

def imprimir_mensagem(qt_palavras):
    print(f"A quantdade de palavras é: {qt_palavras}.")
    
imprimir_mensagem(contar_palavras(converter_em_lista(ler_texto())))