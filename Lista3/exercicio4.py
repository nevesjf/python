#EXERCICIO 4

num = int(input("Digite o valor: "))
k = 1
prox = 1
a = 1

while a <= num-2:
	k = prox
	prox = k + prox
	a += 1
	
print(prox)	
