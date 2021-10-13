tip = int(input("Opções: \n"
                "[1] Metros \n"
                "[2] Centímetros\n"
                "[3] Milímetros\n"))

m =int(input("Escolha a opção para converter: \n"
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


elif tip == 2 and m == 3:
    print(f"O valor de {n2}cm é de {n2 * 1000}mm")
elif tip == 3 and m == 1:
    print(f"O valor de {n2}mm é de {n2 / 1000 }M")

elif tip == 3 and m == 2:
    print(f"O valor de {n2}mm é de {n2 / 100}cm")

elif tip == 3 and m == 3:
    print("Não ha conversão!!")









