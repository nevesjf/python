#1 lata pinta 54 metros
qtdMetros = int(input("Entre com a qtd de metro: "))
if qtdMetros % 54 == 0:
    latas = qtdMetros/54
else:
    latas = int(qtdMetros/54) + 1

print("Serao necessarias : " + str(latas) + " latas")

