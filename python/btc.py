import requests
from tkinter import *
r=requests.get('https://www.mercadobitcoin.net/api/BTC/ticker').json()
preco =round(float((r['ticker']['last'])),2)

btc = 0.00777167
rend= round(btc*preco,2)
msg = "Você tem R$"  +str(rend)+" em bitcoins."
def at():
	r=requests.get('https://www.mercadobitcoin.net/api/BTC/ticker').json()
	preco =round(float((r['ticker']['last'])),2)
	btc = 0.00777167
	rend= round(btc*preco,2)
	msg = "Você tem R$"  +str(rend)+" em bitcoins."
	label.configure(text=msg)
	label.pack()
	

app=Tk()
titulo=Label(app,text='INVESTIMENTOS', pady=20).pack()
label=Label(app,text=msg,pady=20)
label.pack()
btn = Button(app, text= 'atualizar',command=at,bg="#aaeeee", fg='#229')
btn.pack()
app.mainloop()
