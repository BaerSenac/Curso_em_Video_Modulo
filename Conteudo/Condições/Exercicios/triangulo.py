a = float(input("Digite um lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR trinângulo!")
else:
    print("Os segmentos acima NÂO PODEM FORMAR triângulo!")