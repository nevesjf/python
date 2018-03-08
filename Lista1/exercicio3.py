#EXERCICIO3
vlrDias = int(input("Entre com a qtd de dias: "))
vlrHoras = int(input("Entre com a qtd de horas: "))
vlrMinutos = int(input("Entre com a qtd de minutos: "))
vlrSegundos = int(input("Entre com a qtd de segundos: "))

#Conversão
conv = vlrDias*24*60*60+vlrHoras*60*60+vlrMinutos*60+vlrSegundos
print("O valor em segundos é: ", conv)