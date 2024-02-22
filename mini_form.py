from tkinter import*

janela=Tk()
janela.title('mini formulario')
janela.geometry('400x500')
janela.iconbitmap('icons8-capivara-48.ico')

def selecao():
    tag['text']='Estado de '+lista.get(ANCHOR)

nome=Label(janela,text='Insira seu nome')
nome.pack()
caixa=Entry(janela)
caixa.pack()

genero=Label(janela,text='Qual seu genêro?')
genero.pack()

var=IntVar()
r1=Radiobutton(janela,text='Feminino',variable=var,value=1)
r1.pack()

r2=Radiobutton(janela,text='Masculino',variable=var,value=2)
r2.pack()

r3=Radiobutton(janela,text='Não binário',variable=var,value=3)
r3.pack()

r4=Radiobutton(janela,text='Prefiro não informar',variable=var,value=4)
r4.pack()

lista=Listbox(janela)
frame = Frame(janela)
sb=Scrollbar(frame,orient=VERTICAL)
lista=Listbox(frame,
              width=35,height=10,
              yscrollcommand=Scrollbar.set)
sb.config(command=lista.yview)
sb.pack(side=RIGHT,fill=Y)
mylist=['Acre',
    'Alagoas',
    'Amapá',
    'Amazonas',
    'Bahia',
    'Ceará',
    'Distrito Federal',
    'Espírito Santo', 
    'Goiás',
    'Maranhão',
    'Mato Grosso',
    'Mato Grosso do Sul',
    'Minas Gerais',
    'Pará',
    'Paraíba',
    'Paraná',
    'Pernambuco',
    'Piauí',
    'Rio de Janeiro',
    'Rio Grande do Norte',
    'Rio Grande do Sul',
    'Rondônia',
    'Roraima',
    'Santa Catarina',
    'São Paulo',
    'Sergipe',
    'Tocantins'
]

frame.pack()
lista.pack()

# para cada item adicionado na minha lista vá para o fim dela
for item in mylist:
    lista.insert(END,item)

# mudando oq esta abaixo da lista para o estado selecionado
tag=Label(janela,text=' ')
tag.pack()


btn=Button(janela,text='Enviar',command=quit)
btn.pack()

janela.mainloop()