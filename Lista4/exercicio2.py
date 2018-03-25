#EXERCICIO 2
import random

x, y = 0, 0
arrNums=[]
arrPar=[]
arrImp=[]
while x <= 20:
	arrNums.append(random.randint(1,100))
	x += 1


for y in range(0,20):
	if (int(arrNums[y]) % 2) == 0:
		arrPar.append(int(arrNums[y]))
	else:
		arrImp.append(int(arrNums[y]))
		
print("Array gerado: \n" + str(arrNums))
print("Array par: \n" + str(arrPar))
print("Array impar: \n" + str(arrImp))
	
