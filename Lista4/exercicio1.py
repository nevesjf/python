#EXERCICIO 1
import random

x, y = 0, 0
arrNums=[]
while x <= 10:
	arrNums.append(random.randint(1,100))
	x += 1


maior = int(arrNums[0])
for y in range(0,10):
	atual = int(arrNums[y])
	prox = int(arrNums[int(y + 1)])
	if atual >= maior and atual >= prox:
		maior = atual
	elif prox >= maior:
		maior = prox
print(arrNums)
print("O maior numero do array é: ", maior)
	
