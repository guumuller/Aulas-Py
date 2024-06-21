# Desafio 2
# Crie um código que imprima o triangulo abaixo.
# lendo a quantidade de linhas.


         #
        ##
       ###
      ####
     #####
    ######
   #######
  ########
 #########
##########


qt = int(input("Quantidade de linhas: "))

for i in range(qt + 1):
    print(" " * (qt - i) + "#" * i )