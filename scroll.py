from tkinter import *
janela=Tk()
janela.title('ScrollBar')
janela.iconbitmap('icons8-capivara-48.ico')
janela.geometry('500x400+50+50')

def selecao():
    tag['text']='Estado de '+lista.get(ANCHOR)

# montando a lista
lista=Listbox(janela)


# frame para exibir o scrollbar dentro da lista
frame = Frame(janela)

# orientaçao na vertical
sb=Scrollbar(frame,orient=VERTICAL)

# rolagem na vertical e .set para faze lo funcionar
lista=Listbox(frame,width=20,height=10,yscrollcommand=Scrollbar.set)

# a visibilidade da barra de rolagem dentro da lista estara na vertical
sb.config(command=lista.yview)

# sera exibido a direta da lista
sb.pack(side=RIGHT,fill=Y)

#  a lista
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

# botao de selecionar o estado
btn=Button(janela,text='Selecionar',command=selecao)
btn.pack()



janela.mainloop()