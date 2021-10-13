n1 = float(input("Digite a nota do aluno: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1 + n2 + n3) / 3
print("Primeira nota foi: {}\n"
      "Segunda nota foi: {}\n"
      "Terceira nota foi: {}\n"
      "A média do aluno foi de {:.3f}".format(n1,n2,n3,media))
