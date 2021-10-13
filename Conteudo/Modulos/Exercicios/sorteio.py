import random
'''n1 = input("Digite um nome: ")
n2 = input("Digite o segundo nome: ")
n3 = input("Digite o terceiro nome: ")
n4 = input("Digite o quarto nome:   ")
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("O escolhido foi: {}".format(escolhido))'''

n1 = input("Digite um nome: ")
n2 = input("Digite o segundo nome: ")
n3 = input("Digite o terceiro nome: ")
n4 = input("Digite o quarto nome:   ")
lista = [n1, n2, n3, n4]
escolhidos = random.shuffle(lista)
print("A ordem de aprensentação:  ")
print(lista)