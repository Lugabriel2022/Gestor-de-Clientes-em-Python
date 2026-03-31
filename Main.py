import tkinter as tk
from tkinter import ttk
from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from Utils import Funcs, Base
from Report import Relatórios


class Application(Funcs, Relatórios):
    def __init__(self): #cira a função de inicialização da janela
        self.jan = tk.Tk() #gera uma equivalencia lembrando o programa que jan se refere a jenela
        self.db = create_engine("sqlite:///Curso Python/Python casa/Praticas/CRUD/clientes.db")
        Session = sessionmaker(bind = self.db)
        self.session = Session()
        Base.metadata.create_all(bind = self.db)
        self.tela() #chama as configuração inseridas dentro da função tela
        self.frame_da_tela()
        self.widget_frame1()
        self.widget_frame2()
        self.atualizar_treeview()
        self.Menus()
        self.jan.mainloop() #cria o loop da janela

    def tela(self): #cria a função tela
        self.jan.title('Cadastro Clientes')#define o titulo da janela
        self.jan.configure(background= '#1e3743') #define a cor do backgtound da janela usado códigos hexa decimais ou cores pré setadas
        self.jan.geometry('700x500') #define o tamanho inicial da janela, sendo sempre (largura x altura)
        self.jan.resizable(True, True) #define se a janela sera responsiva ou não
        self.jan.maxsize(width = 900, height= 700) #define o tamanho limite da tela, sendo sempre (largura x altura)
        self.jan.minsize(width= 600, height= 400) #define o tamanho minimo da tela, sendo sempre (largura x altura)

    def frame_da_tela(self):
        self.frame_1 = tk.Frame(self.jan, bd = 4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness= 2) #cria um frame
        self.frame_1.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.46) #define o tamanho, posição e coloca o frame na janela
        self.frame_2 = tk.Frame(self.jan, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widget_frame1(self): ###Criação do botão limpar
        self.bt_limpar = tk.Button(self.frame_1, text= 'Limpar', bd= 4, bg= '#F0E68C', fg= '#00008B', font = ('Comic Sans MS', 8, 'bold'), command = self.limpa_tela)
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15) #botão buscar
        self.bt_buscar = tk.Button(self.frame_1, text= 'Buscar', bd= 4, bg= '#F0E68C', fg= '#00008B', font = ('Comic Sans MS', 8, 'bold'))
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15) #botão novo
        self.bt_novo = tk.Button(self.frame_1, text= 'Novo', bd= 4, bg= '#F0E68C', fg= '#00008B', font = ('Comic Sans MS', 8, 'bold'), command = self.adicionar)
        self.bt_novo.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15) #botão alterar
        self.bt_alt = tk.Button(self.frame_1, text= 'Alterar', bd= 4, bg= '#F0E68C', fg= '#00008B', font = ('Comic Sans MS', 8, 'bold'), command = self.editar)
        self.bt_alt.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #botão apagar
        self.bt_apagar = tk.Button(self.frame_1, text= 'Apagar', bd= 4, bg= '#F0E68C', fg= '#00008B', font = ('Comic Sans MS', 8, 'bold'), command = self.remover)
        self.bt_apagar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15) #Criação da label e entrafa do codigo
        self.lb_codigo = tk.Label(self.frame_1, text= 'Código', bg= '#dfe3ee', fg= '#00008B', font = ('Comic Sans MS', 8, 'bold'))# bg é a cor do fundo, fg é a cor do texto, font é a fonte do texto
        self.lb_codigo.place(relx= 0.05, rely=0.05)
        self.codigo_entry = tk.Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)
        #criação da label e entrada do nome
        self.lb_nome = tk.Label(self.frame_1, text= 'Nome', bg= '#dfe3ee', fg= '#00008B', font = ('Comic Sans MS', 8, 'bold'))
        self.lb_nome.place(relx= 0.05, rely= 0.35) #rel significativa relativo, ou seja relx significa que a posição é relativa a posição x da janela ou no caso do frame
        self.nome_entry = tk.Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.8) #relwidth quer dizer que a largura é relativaa a lagura do frame
        # #criação label e entrada telefone
        self.lb_tel = tk.Label(self.frame_1, text= 'Telefone', bg= '#dfe3ee', fg= '#00008B', font = ('Comic Sans MS', 8, 'bold'))
        self.lb_tel.place(relx= 0.05, rely= 0.55)
        self.tel_entry = tk.Entry(self.frame_1)
        self.tel_entry.place(relx= 0.05, rely= 0.65, relwidth= 0.4)
        #criação label e entrada cidade
        self.lb_city = tk.Label(self.frame_1, text= 'Cidade', bg= '#dfe3ee', fg= '#00008B', font = ('Comic Sans MS', 8, 'bold'))
        self.lb_city.place(relx = 0.5, rely= 0.55)
        self.city_entry = tk.Entry(self.frame_1)
        self.city_entry.place(relx= 0.5, rely= 0.65, relwidth= 0.4)

    def widget_frame2(self):
        #criando a treeview
        self.listacli = ttk.Treeview(self.frame_2, height = 4, column = ('col1', 'col2', 'col4', 'col4')) #ttk é um modulo avançado do tkinter e deve ser importado separadamente, a treeview ´w uma lsita simples no questio que existem mais avançados
        self.listacli.heading('#0', text = '')
        self.listacli.heading('#1', text = 'Código')
        self.listacli.heading('#2', text = 'Nome')
        self.listacli.heading('#3', text = 'Telefone')
        self.listacli.heading('#4', text = 'Cidade')
        self.listacli.column('#0', width = 1)
        self.listacli.column('#1', width = 50)
        self.listacli.column('#2', width = 200)
        self.listacli.column('#3', width = 125)
        self.listacli.column('#4', width = 125)
        self.listacli.place(relx = 0.01, rely = 0.01, relwidth = 0.95, relheight = 0.85)
        self.scroollista = tk.Scrollbar(self.frame_2, orient='vertical')
        self.listacli.configure(yscroll=self.scroollista.set)
        self.scroollista.place(relx = 0.96, rely = 0.01, relwidth = 0.04, relheight = 0.85)
        self.listacli.bind('<Double-1>', self.OnDoubledClick)

    def Menus(self):
        menubar = tk.Menu(self.jan)
        self.jan.config(menu = menubar)
        filemenu = tk.Menu(menubar, tearoff = 0)
        sobremenu = tk.Menu(menubar, tearoff = 0)
        reportmenu = tk.Menu(menubar, tearoff = 0)

        def Quit(): 
            self.jan.destroy()

        menubar.add_cascade(label = 'Opções', menu = filemenu)
        menubar.add_cascade(label = "Sobre", menu = sobremenu)
        menubar.add_cascade(label = "Relatórios", menu = reportmenu)

        filemenu.add_command(label = "Sair", command= Quit)
        sobremenu.add_command(label = "Limpar Cliente", command= self.limpa_tela)
        reportmenu.add_command(label = "Ficha do Cliente", command= self.gerarRelatCliente )

Application()