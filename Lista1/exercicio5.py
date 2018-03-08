#EXERCICIO5
vlrMercadoria = float(input("Valor mercadoria: "))
pctDesc = int(input("Porcentagem de desconto: "))

vlrDesc = vlrMercadoria*pctDesc/100
vlrFinal = vlrMercadoria-vlrDesc
print("Valor do desconto: R$"+ str(vlrDesc) + " | Total: R$", vlrFinal)