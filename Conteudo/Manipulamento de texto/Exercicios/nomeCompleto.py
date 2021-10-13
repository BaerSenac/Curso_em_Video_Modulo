nome = str(input("Digite seu nome:  ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiúsculas é: {}".format(nome.upper()))
print("Seu nome em minúsculas é: {}".format(nome.lower()))
print("Seu nome tem ao todo: {}".format(len(nome) - nome.count(" ")))
print("seu primeiro nome tem: {}".format(nome.find(" ")))

