#EXERCICIO 3
#peixe > 50kg paga taxa de R$4/kilo

pesoPeixe = int(input("Peso do peixe: "))
if pesoPeixe > 50:
    multa = (pesoPeixe - 50) * 4
else:
    multa = 0

print(f'A multa a ser paga para {pesoPeixe} kg e de R${multa}')

