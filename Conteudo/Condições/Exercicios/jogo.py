from random import randint
from time import sleep

computador = randint(0, 10)
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 10, tente adivinhar...")  # Computador está sorteando um numero#
print("-=-" * 20)
sleep(3)

jogador = int(input("Qual número eu escolhi? "))                   # Jogador escolhe um valor#

print("Espera que o pai ta verificando...")
sleep(3)

if jogador == computador:
    print("Omedetooo , você ganhou tigrão!!")
else:
    print(f"Perdeu otário, eu escolhi {computador}")
