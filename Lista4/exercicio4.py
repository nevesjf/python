#EXERCICIO 4
import string
texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

texto = texto.replace(",", " ")
texto = texto.replace(".", " ")
texto = texto.replace(":", " ")
texto = texto.replace("  ", " ")
texto = texto.split()

arrPy = ["P", "p", "Y","y","T","t","H","h","O","o","N","n"]
x, y = 0, 0
lista = []
primLetra = []
ultLetra = []

while x < len(texto):
	primLetra.append(texto[x][:1])
	ultLetra.append(texto[x][-1])
	x += 1
	

for y in range(0,11):
		for z in range(0,(len(texto))):
			#print("Primeira letra: " + primLetra[z] + " Ultima Letra: " + ultLetra[z] + " Letra array Py: " + arrPy[y] + " Palavra: " + texto[z])
			if primLetra[z] == arrPy[y] or ultLetra[z] == arrPy[y]:
				lista.append(texto[z])
				
#print("Texto: \n" , texto)
#print("Primeira Letra: \n" , primLetra)
#print("Ultima Letra: \n" , ultLetra)
print("Lista Final: \n" , lista)
