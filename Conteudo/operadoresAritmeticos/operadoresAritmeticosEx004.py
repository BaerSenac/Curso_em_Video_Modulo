# Conteudo Aritméticos

# Aonde insere os valores
n1 = int(input(" Um valor: "))
n2 = int(input(" Outro valor: "))

# Criação das variaveis
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
restodivisao = n1 // n2
potencia = n1 ** n2

# O que sera mostrado no terminal
print(" A soma é: {},\n o produto é: {} \n divisão é: {:.3f}".format(soma,multiplicacao,divisao), end=' ')
print(" Divisão inteira {}, e potência {}".format(restodivisao,potencia))
