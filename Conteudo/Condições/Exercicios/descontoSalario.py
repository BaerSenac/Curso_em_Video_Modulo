salario = float(input("Digite o valor do salário a ser calculado: "))
descontoAcima = (salario * 10) / 100
descontoAbaixo = (salario * 15) / 100
if salario > 1250:
    print(f"O aumento do salario será de {descontoAcima}\n"
          f"totalizando {descontoAcima + salario}")
else:
    print(f"O aumento do salario será de {descontoAbaixo + salario}")