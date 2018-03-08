#EXERCICIO1
num1 = int(input("Entre com um numero inteiro: "))
num2 = int(input("Entre com outro numero inteiro: "))
soma = num1 + num2
print("A soma de " + str(num1) + " e "+ str(num2) + " é: ", soma)

#EXERCICIO2
valorMetros = float(input("Entre com valor em metros: "))
valorMilimetros = valorMetros * 1000
print("O valor em milimetros de " + str(valorMetros) + " é: ", valorMilimetros)

#EXERCICIO3
vlrDias = int(input("Entre com a qtd de dias: "))
vlrHoras = int(input("Entre com a qtd de horas: "))
vlrMinutos = int(input("Entre com a qtd de minutos: "))
vlrSegundos = int(input("Entre com a qtd de segundos: "))

#Conversão
conv = vlrDias*24*60*60+vlrHoras*60*60+vlrMinutos*60+vlrSegundos
print("O valor em segundos é: ", conv)

#EXERCICIO4
vlrSalario = float(input("Valor do salario: "))
pctAumento = int(input("Porcentagem de aumento: "))

novoSalario = vlrSalario+vlrSalario*pctAumento/100
print("Novo salário é: ", novoSalario)

#EXERCICIO5
vlrMercadoria = float(input("Valor mercadoria: "))
pctDesc = int(input("Porcentagem de desconto: "))

vlrDesc = vlrMercadoria*pctDesc/100
vlrFinal = vlrMercadoria-vlrDesc
print("Valor do desconto: R$"+ str(vlrDesc) + " | Total: R$", vlrFinal)

#EXERCICIO6
dist = float(input("Entre com a distância(KM): "))
vlMedia = int(input("Entre com a velocidade média(KM/H): "))

#v=d/t => t=d/v

tempoViagem = dist/vlMedia

print("Tempo de viagem é de: " + str(tempoViagem) + "H")

#EXERCICIO7
tmpC = float(input("Entre com valor em °C: "))
tmpF = (9*tmpC)/5+32
print("A temperatura em F de " + str(tmpC) + "°C é de: " + str(tmpF) + "F")

#EXERCICIO8
tmpF = float(input("Entre com valor em F: "))
tmpC = (tmpF-32)/1.8
print("A temperatura em °C de " + str(tmpF) + "F é de: " + str(tmpC) + "°C")

#EXERCICIO9
kmPercorrido = float(input("Qtd KM percorrido: "))
qtdDias = int(input("Qtd dias locaçao: "))

totalLocacao = kmPercorrido*0.15+qtdDias*60
print("Total: R$", totalLocacao)

#EXERCICIO10
qtdCigarros = int(input("Qtd cigarros por dia: "))
tmpFumante = int(input("Qtd de anos que fuma: "))

#total de cigarros por ano
qtdTotalCigarros = qtdCigarros*365*tmpFumante

tmpVida = ((qtdTotalCigarros*10)/24)/60
print('Tempo de vida perdido: ', tmpVida)

#EXERCICIO11
print(len(str(2**1000000)))

