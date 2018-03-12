edificio = ["Familia Souza","Familia Brito", "Sr Jorge", "Familia Tanaka"]
print(edificio[0])
print(edificio[1])
print(edificio[2])
print(edificio[3])

edificio.append("Dona Chica") #Insere item
edificio.append("Ze das Couve")

print(edificio)

if 'Ze das Couve' in edificio:
    edificio.remove("Dona Chica") #Remove

print(edificio)