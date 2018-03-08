#EXERCICIO6
dist = float(input("Entre com a distância(KM): "))
vlMedia = int(input("Entre com a velocidade média(KM/H): "))

#v=d/t => t=d/v

tempoViagem = dist/vlMedia

print("Tempo de viagem é de: " + str(tempoViagem) + "H")