#EXERCICIO 5
num1 = int(input("Digite primeiro numero: "))
num2 = int(input("Digite segundo numero: "))

ant=num1
prox=num2
result=ant % prox

while result != 0:
    ant = prox
    prox=result
    result=ant % prox
    
print("O MDC de %d e %d = %d" % (num1,num2,prox))
