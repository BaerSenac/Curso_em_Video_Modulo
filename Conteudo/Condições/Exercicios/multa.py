velocidade = float(input("Digite a velocidade que o carro ultrapassou: "))
if velocidade >80:
    print("MULTADO!! Você excedeu o limite permitido que é de 80Km/h")
    multa = (velocidade - 80) * 7
    print("Voce deve pagar uma multa de R${:.2f}".format(multa))
else:
    print("Você esta no limite")

print("Tenha um bom dia e dirija com seguraça")