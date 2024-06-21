# Desafio 3
# Crie um código que imprima o triangulo abaixo.
# lendo a quantidade de linhas.


         #
        ###
       #####
      #######
     #########
    ###########
   #############
  ###############
 #################
###################

def triangulo(qt_linhas):
    for i in range(qt_linhas):
        espacos = (qt_linhas - i - 1)
        caracteres = 2 * i + 1
        linha = " " * espacos + "#" * caracteres
        print(linha)

qt_linhas = int(input("Digite a quantidade de linhas do triângulo: "))
triangulo(qt_linhas)