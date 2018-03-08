#EXERCICIO9
kmPercorrido = float(input("Qtd KM percorrido: "))
qtdDias = int(input("Qtd dias locaçao: "))

totalLocacao = kmPercorrido*0.15+qtdDias*60
print("Total: R$", totalLocacao)