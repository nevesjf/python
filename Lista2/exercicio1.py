#EXERCICIO1

ladoA = int(input("Entre com o valor do primeiro lado: "))
ladoB = int(input("Entre com o valor do segundo lado: "))
ladoC = int(input("Entre com o valor do terceiro lado: "))


if ladoC>(ladoA + ladoB) or ladoB>(ladoA + ladoC) or ladoA>(ladoC + ladoB) :
    print("Não é um triangulo! ")
elif ladoA == ladoB and ladoA == ladoC :
    print("Triangulo Equilátero! ")
elif ladoA != ladoB or ladoA != ladoC or ladoB != ladoC :
    print("Triangulo escaleno! ")
else: 
    print("Triangulo Isósceles! ")

