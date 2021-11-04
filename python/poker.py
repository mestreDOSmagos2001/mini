import random 
numeros = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
naipe =[" de Copas"," de Ouro"," de Paus"," de Espadas"]
baralho =[]
for nai in naipe:
	for num in numeros:
		carta = str(num)+nai
		baralho.append(carta)

def mao():
	sorteada= random.choice(baralho)
	baralho.remove(sorteada)
	return sorteada

minhas_fichas= 1000
adv_fichas=1000
s_blind=10
b_blind= 2*s_blind
pote=0
def check():
	pass
def bet_eu(minhas_fichas,pote, bet):
	minhas_fichas=minhas_fichas - bet
	pote=pote+bet
	return minhas_fichas, pote
	
	
carta1=mao()
carta2=mao()
mão=[carta1,carta2]


carta3=mao()
carta4=mao()

mão_adv=[carta3,carta4]

carta5=mao()
carta6=mao()
carta7=mao()
carta8=mao()
carta9=mao()

print("Suas cartas fechadas são: ")
print(mão)
mesa=[carta5,carta6,carta7]

print("Flop: ")
print(mesa)
mesa.append(carta8)
print("Turn: ")
print(mesa)
mesa.append(carta9)
print("River: ")
print(mesa)
print("Mão do adversário: ")
print(mão_adv)
print(bet_eu(minhas_fichas,pote,300))