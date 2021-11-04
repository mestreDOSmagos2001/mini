from tkinter import Tk, Label, Button,StringVar,Entry
from random import randrange
mao1 = randrange(0,4)
def soma():
	total=int(mao.get())+mao1
	lbmao1.configure(text="Outro Show tem %d na mão e você tem %s"%(mao1,mao.get()))
	lbmao1.pack()
	lbtotal.configure(text='Total é %d e você pediu %s'%(total,palpite.get()))
	lbtotal.pack()
	if (int(palpite.get())==total):
		final.config(text='***VENCEU!***',fg='green')
		final.pack()
	else:
		final.config(text='***PERDEU!***',fg='red')
		final.pack()

app=Tk()

mao=StringVar()
palpite=StringVar()
Label(app,text='SUA MÃO').pack()
mao_entry = Entry(app, textvariable=mao)
mao_entry.pack()
mao_entry.focus()
Label(app,text='SEU PALPITE').pack()
palpite_entry=Entry(app, textvariable=palpite)
palpite_entry.pack()
btn=Button(app, text='jogar',command=soma)
btn.pack()
lbmao1=Label(app)
lbtotal=Label(app)
final=Label(app)
app.mainloop()