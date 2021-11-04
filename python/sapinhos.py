from random import randrange
from random import choice
cores=['white','blue','green','yellow','red','brown','purple','pink','#f46a21']
formas=['quadrado','triangulo','bola','retangulo','losango','listas','coracao','exclamacao','cifrao']
class Sapo:
	def __init__ (self, cor, desenho, cordodesenho):
		self.cor=cor
		self.desenho=desenho
		self.cordodesenho=cordodesenho
print("pai")
print("---------------")		
sapinho=Sapo(choice(cores),choice(formas),choice(cores))
print(sapinho.cor,sapinho.desenho,sapinho.cordodesenho)
print("---------------")
print("mae")
print("---------------")

sapinho2=Sapo(choice(cores),choice(formas),choice(cores))
print(sapinho2.cor,sapinho2.desenho,sapinho2.cordodesenho)
print("--------------")

def cruzar(a,b):
	cor=""
	desenho=""
	cordodesenho=""
	x = randrange(1,3)
	y=randrange(1,3)
	z=randrange(1,3)
	if x==1:
		cor=a.cor
	else:
		cor=b.cor
	if y==1:
		desenho=a.desenho
	else:
		desenho=b.desenho
	if z==1:
		cordodesenho=a.cordodesenho
	else:
		cordodesenho=b.cordodesenho
	return cor, desenho, cordodesenho
	
print('filhotes')
print('------------------')		

resultado=(cruzar(sapinho,sapinho2))
filhote =Sapo(resultado[0],resultado[1],resultado[2])
print(filhote.cor,filhote.desenho,filhote.	cordodesenho)



	
	