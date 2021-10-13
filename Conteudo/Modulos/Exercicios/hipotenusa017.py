import math
co = float(input("Digite o comprimento do cateto oposto:"))
ca = float(input("Digite o comprimento do cate adjacente: "))
hi = math.hypot(co, ca)
print(f"Com os valores do cateto oposto {co}, e cateto adjacente {ca}, o resultado do comprimento da hipotenusa é de {hi:.2f}")
