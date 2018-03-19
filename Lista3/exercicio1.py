#EXERCICIO 1
nota = int(input("Insira uma nota entre 0 e 10: "))
a = 0
while a == 0:
    if nota >= 0 and nota <= 10:
        print("Ok!")
        a = 1
    else:
        a = 0
        print("Valor invalido! Digite novamente...")
        nota = int(input("Insira uma nota entre 0 e 10: "))
