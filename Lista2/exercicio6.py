vlrPorHora = float(input("Valor por hora: "))
horasTrabalhadas = float(input("Horas trabalhadas: "))
txIR = 11/100
txINSS = 8/100
txSind = 5/100

salBruto = vlrPorHora * horasTrabalhadas
vlrIR = salBruto * txIR
vlrINSS = salBruto * txINSS
vlrSind = salBruto * txSind
salLiq = salBruto - (vlrIR+vlrINSS+vlrSind)

print("+ Salario Bruto: R$", salBruto)
print("- IR (11%): R$", vlrIR)
print("- INSS (8%): R$", vlrINSS)
print("- Sindicato (5%): R$", vlrSind)
print("= Salario Liquido: R$", salLiq)

