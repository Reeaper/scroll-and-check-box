from tkinter import *
janela=Tk()
janela.iconbitmap('icons8-capivara-48.ico')
janela.title('CheckBox com Formatação')
janela.geometry('500x500+100+100')
janela['bg']=['#6959CD']

def funcao():
    # define a resposta exibida se selecionar ou nao um checkbox
    if v1.get()==1:
        tag1['text']='Opção um selecionada'
    elif v1.get()==0 and v2.get()==0:
        tag1['text']='Selecione ao menos uma opção'
    else:
        tag1['text']=''

    if v2.get()==1:
        tag2['text']='Opção dois selecionada'
    else:
        tag2['text']=''
    
# label pra alinhar os checkbox usando grid
espaco=Label(janela,text='',bg='#6959CD').grid(padx=(100,100))

v1=IntVar()
Checkbutton(janela,
            text='Opção 1',
            variable=v1,
            relief='sunken',
            bg='#483D8B',
            fg='#F8F8FF').grid(padx=200,pady=5)
v2=IntVar()
Checkbutton(janela,
            text='Opção 2',
            variable=v2,
            relief='sunken',
            bg='#483D8B',
            fg='#F8F8FF').grid(padx=10,pady=5)

btn=Button(janela,text='Selecionar',command=funcao,
           bg='#6495ED',fg='#F8F8FF')
btn.grid(padx=10)

tag1=Label(janela,text=' ',bg='#6959CD')
tag1.grid(padx=10)

tag2=Label(janela,text=' ',bg='#6959CD')
tag2.grid(padx=10)

janela.mainloop()