from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from random import sample


def clicked():
    lista = []
    for n in range(1, 61):
        lista.append(n)
    sorteados = sample(lista, 6)
    showinfo(message=f'Seus números da sorte da Mega são:\n{sorteados}')


root = Tk()
label = Label(root, text='Números da Mega')
label.pack()
button = Button(root, text='Sortear', command=clicked)
button.pack()
root.mainloop()
