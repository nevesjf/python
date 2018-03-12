#EXERCICIO 5

arrNum=[]
y = 0
while y < 3:
    n = int(input("Entre um numero: "))
    arrNum.append(n)
    y = y+1

maiorNum = max(arrNum)
menorNum = min(arrNum)

print("O menor numero e: ", menorNum)
print("O maior numero e: ", maiorNum)

