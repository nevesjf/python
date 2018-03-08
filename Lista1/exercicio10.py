#EXERCICIO10
qtdCigarros = int(input("Qtd cigarros por dia: "))
tmpFumante = int(input("Qtd de anos que fuma: "))

#total de cigarros por ano
qtdTotalCigarros = qtdCigarros*365*tmpFumante

tmpVida = ((qtdTotalCigarros*10)/24)/60
print('Tempo de vida perdido: ', tmpVida)

