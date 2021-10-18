casa = float(input("Digite o valor da casa R$: "))
salario = float(input("Digite o seu salário R$: "))
ano = int(input("Digite quantos anos você quer financiar: "))

prestação = casa / (ano * 12)
minimo = salario * 30 / 100

print("Para pagar uma casa de R${:.2f} em {} anos".format(casa,ano))
print("A prestação será de {:.2f}".format(prestação))

if prestação <= minimo:
    print("Empréstimo APROVADO")
else:
    print("Empréstimo REPROVADO")