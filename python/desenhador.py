import sapinhos
from tkinter import *
janela =Tk()
canvas = Canvas(janela,width= 720,height= 1280, bg='white')

def desenha_pai(c1,c2):
	pai = canvas.create_oval(50,  50, 200, 		250, fill=c1)
	pai_desenho=canvas.create_oval(100, 	100,150, 200,fill=c2)
	
def desenha_mae(c1,c2):
	mae = canvas.create_oval(250,50,400,		250,fill=c1)
	mae_desenho=canvas.create_oval(300, 	100,350, 200,fill=c2)

def desenha_cria(c1,c2):	
	cria = canvas.create_oval(50, 300, 200,	500,fill=c1)
	cria_desenho=canvas.create_oval(100,	350,150,450,fill=c2)
	
desenha_pai(sapinhos.sapinho.cor,sapinhos.sapinho.cordodesenho)

desenha_mae(sapinhos.sapinho2.cor,sapinhos.sapinho2.cordodesenho)

desenha_cria(sapinhos.filhote.cor,sapinhos.filhote.cordodesenho)	


canvas.pack()
mainloop()