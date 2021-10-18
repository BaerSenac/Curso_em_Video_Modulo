r1 = float(input("Digite um lado: "))
r2 = float(input("Digite um segundo lado: "))
r3 = float(input("Digite um terceiro lado: "))
if r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r1 + r2:
  print("Os segmentos acima PODEM FORMAR UM TRIANGULO!")
else:
  print("Os acima não PODEM FORMAR UM TRIANGULO!")