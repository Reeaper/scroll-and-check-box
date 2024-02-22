from tkinter import*
master = Tk()
master.iconbitmap('icons8-capivara-48.ico')
master.title('Check Box')


male=IntVar()
Checkbutton(master,text='Homem',variable=male).grid(row=0,sticky=W)

# checkbox com grid 
female=IntVar()
Checkbutton(master,
            text='Mulher',
            variable=female).grid(row=1,sticky=W)

nonbinary=IntVar()
Checkbutton(master,
            text='Não-Binário',
            variable=nonbinary).grid(row=2,sticky=W)

noinfo=IntVar()
Checkbutton(master,
            text='Prefiro não informar',
            variable=noinfo).grid(row=3,sticky=W)

mainloop()