import opcode

print("FERRAMENTA DE OPERAÇÕES")

op = int(input("[1] Calculadora\n"
               "[2] Coversor de Moedas\n"
               "[3] Tabuada\n"
               "[4] Conversor de medidas\n"
               "Escolha uma opção:  "))

if op == 1:

    op1 = int(input("Escolha a operação:\n"
                    "[1] = +\n"
                    "[2] = -\n"
                    "[3] = *\n"
                    "[4] = /\n"))

    v = float(input("Insira um valor: "))
    v2 = float(input("Insira outro valor: "))

    if op1 == 1:
        print(f"O resultado da soma de {v} + {v2} é:\n {v + v2:.3f}")

    elif op1 == 2:
        print(f"O resultado da subtração de {v} - {v2} é:\n {v - v2:.3f}")

    elif op1 == 3:
        print(f"O resultado da multiplicação de {v} x {v2} é:\n {v * v2:.3f}")

    elif op1 == 4:
        print(f"O resultado da divisão de {v} / {v2} é:\n {v / v2:.3f}")

elif op == 2:

    n1 = float(input("Saldo para coverter: "))
    op2 = int(input("Escolha o tipo da moeda: \n"
                    "[1] Conversão de Real para Dolar\n"
                    "[2] Conversão de Dolar para Real\n"))
    if op2 == 1:
        print(f"O seu valor de R${n1} em Dolar é: US${n1 / 5.40:.2f}")

    else:
        print(f"O seu valor de US${n1} em Reais é: R${n1 / 0.18:.2f}")

elif op == 3:
    num = int(input("Digite o valor da tabuada: "))

    for n in range(11):
        print(f"{num} x {n} = {num * n}")

elif op == 4:
    tip = int(input("Opções: \n"
                    "[1] Metros \n"
                    "[2] Centímetros\n"
                    "[3] Milímetros\n"))

    m = int(input("Escolha a opção para converter: \n"
                  "[1] Metros\n"
                  "[2] Centímetros\n"
                  "[3] Milímetros\n"))

    n2 = int(input("Insira o valor: "))

    if tip == m:
        print("Não ha conversão!!")

    elif tip == 1 and m == 2:
        print(f"O valor de {n2}M é de {n2 * 100}cm")

    elif tip == 1 and m == 3:
        print(f"O valor de {n2}M é de {n2 * 1000}mm")


    elif tip == 2 and m == 1:
        print(f"O valor de {n2}cm é de: {n2 * 100}M")

    elif tip == 2 and m == 2:
        print("Não ha conversão!!")

