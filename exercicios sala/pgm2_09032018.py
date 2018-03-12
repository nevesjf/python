notas = [6,7,5,8,9]
#notas = int(input("Digite as notas: "))

soma = 0
x=0
while x < 5:
    soma += notas[x]
    x += 1
print('Media: %5.2f' %(soma/x))

#Com entrada do usuario
notas2=[]
soma2 = 0
y = 0
while y < 5:
    n = int(input("Entre com a nota: "))
    notas2.append(n)
    soma2 += notas2[y]
    y = y+1
print("As notas sao: ", notas2)
print("A media e: ", soma2/y)
