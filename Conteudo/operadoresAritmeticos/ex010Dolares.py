n1 = float(input("Valor para coversão: "))
b = int(input("Escolha o tipo da moeda: \n"
              "[1] Conversão de Real para Dolar\n"
              "[2] Conversão de Dolar para Real\n"))
if b == 1:
    print(f"O seu valor de R${n1} em Dolar é: US${n1/5.40:.2f}")

else:
    print(f"O seu valor de US${n1} em Reais é: R${n1/0.18:.2f}")
