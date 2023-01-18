from tkinter import *
from time import sleep
from pyautogui import *


def start():
    sleep(3)
    for c in range(int(num.get())):
        write(texto.get())
        sleep(0.1)
        press('enter')
        sleep(0.1)

root = Tk()
root.title('Spammer')

intro = LabelFrame(text='What do you want to send?')
texto = Entry(intro, borderwidth=3, width=30)
intro2 = LabelFrame(text='How many times?')
num = Entry(intro2, borderwidth=3, width=30)
init = Button(text='Start spam', command=start, padx=19)
bq = Button(text='Quit', command=root.quit)

intro.grid(row=0, column=0, padx=7)
texto.grid(row=1, column=0)

intro2.grid(row=0, column=1, padx=7)
num.grid(row=1, column=1)

init.grid(row=2, column=3)
bq.grid(row=3, column=3, sticky='E')

root.mainloop()
