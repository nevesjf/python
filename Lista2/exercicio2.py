#EXERCICIO 2
ano = int(input("Entre com o ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("O ano e bisexto! ")
else:
    print("Nao e bisexto!")

