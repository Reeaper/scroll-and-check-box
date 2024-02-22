from tkinter import*
janela=Tk()
janela.iconbitmap('icons8-capivara-48.ico')
janela.title('RadioButton')
janela.geometry('450x450')
janela['bg']='#F8F8FF'

def selecao():
    Selecionado='Selecionou: '+ str(va.get())
    tag['text']=Selecionado
    
# botao de radio 1
# declarar somente uma variavel para todos os radios
va=IntVar()
rb1=Radiobutton(janela,
               text='Op 1',
               variable=va,
               value=1)
rb1.pack()

# botao de radio 2
rb2=Radiobutton(janela,
               text='Op 2',
               variable=va,
               value=2)
rb2.pack()

# botao de radio 3
rb3=Radiobutton(janela,
               text='Op 3',
               variable=va,
               value=3)
rb3.pack()

# label de seleçao
tag=Label(janela,text='')
tag.pack()

btn=Button(janela,text='Selecione',command=selecao)
btn.pack()

janela.mainloop()