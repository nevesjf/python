#EXERCICIO 3

paisA = 80000
paisB = 200000
cresA = 3/100
cresB = 1.5/100

popA = paisA * cresA
popB = paisB * cresB
k = 1

while popA <= popB:
	popA += popA * cresA
	popB += popB * cresB
	k += 1
print(k)
print(popA)
print(popB)
print("A população A terá "+str(popA)+" e a População B terá "+str(popB)+" em um total de "+str(k)+" anos")
