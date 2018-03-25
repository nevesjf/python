#EXERCICIO 3
import random

x, y = 0, 0
arrNums1=[]
arrNums2=[]
arrNums3=[]
while x <= 10:
	arrNums1.append(random.randint(1,100))
	arrNums2.append(random.randint(1,100))
	x += 1


for y in range(0,10):
	arrNums3.append(arrNums1[y])
	arrNums3.append(arrNums2[y])

print("Primeiro array gerado: \n" + str(arrNums1))
print("Segundo array gerado: \n" + str(arrNums2))
print("Combinação: \n" + str(arrNums3))
	
