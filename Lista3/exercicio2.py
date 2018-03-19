#EXERCICIO 2
a = 1
while a == 1:
    usu = input("Usuario: ")
    senha = input("Senha: ")
    if usu == senha:
        print("Padrao nao aceito! Tente novamente")
        
        a = 1
    else:
        print("Login OK!")
        a =0
