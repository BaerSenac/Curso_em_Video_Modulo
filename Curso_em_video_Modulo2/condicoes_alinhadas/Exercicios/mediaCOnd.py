
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"A primeira nota foi: {n1} e a segunda: {n2}, sua média sera de {media}")
if media >= 7:
    print("O aluno foi APROVADO")
elif media == 5 and 6.9:
    print("O aluno esta de RECUPERAÇÂO")
else:
    print("O aluno esta REPROVADO")
