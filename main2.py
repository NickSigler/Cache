from tkinter import *

janela = Tk()
janela.minsize(width=600, height=800)

frame_esquerda = Frame(janela, width=200, height=600, bg="red").pack(side="left")

lb_processador = Label(frame_esquerda, text="Olá, mundo").pack()



frame_meio= Frame(janela, width=200, height=600, bg="blue").pack(side="left")

lb_processador2 = Label(frame_meio, text="Olá, mundo").pack()



janela.mainloop()