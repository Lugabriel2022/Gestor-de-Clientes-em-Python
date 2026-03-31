from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import tkinter as tk
from tkinter import ttk

Base = declarative_base()
Dados = {
     'Codigo': '',
     'Nome': '',
     'Telefone': '',
     'Cidade': ''
}
class Funcs():
    def adicionar(self):
        Dados['Nome'] = self.nome_entry.get()
        Dados['Telefone'] = self.tel_entry.get()
        Dados['Cidade'] = self.city_entry.get()

        self.novo_cliente = Cliente(Dados['Nome'], Dados['Telefone'], Dados['Cidade'])
        self.session.add(self.novo_cliente)
        self.session.commit()
        self.atualizar_treeview()
        self.limpa_tela()
    
    def remover(self):
        Dados['Codigo'] = int(self.codigo_entry.get())
        usuario = self.session.query(Cliente).filter_by(codigo= Dados['Codigo']).first()
        self.session.delete(usuario)
        self.session.commit()
        self.atualizar_treeview()
        self.limpa_tela()

    def editar(self):
        Dados['Codigo'] = int(self.codigo_entry.get())
        Dados['Nome'] = self.nome_entry.get()
        Dados['Telefone'] = self.tel_entry.get()
        Dados['Cidade'] = self.city_entry.get()
        usuario = self.session.query(Cliente).filter_by(codigo= Dados['Codigo']).first()
        usuario.nome = Dados['Nome']
        usuario.telefone = Dados['Telefone']
        usuario.cidade = Dados['Cidade']
        self.session.commit()
        self.atualizar_treeview()
        self.limpa_tela()

    def atualizar_treeview(self):
    # 1. Limpar Treeview
        for item in self.listacli.get_children():
            self.listacli.delete(item)

        # 2. Buscar registros no banco
        clientes = self.session.query(Cliente).order_by(Cliente.nome).all()

        # 3. Inserir no Treeview
        for cliente in clientes:
            self.listacli.insert(
                "", "end",
                values=(cliente.codigo, cliente.nome, cliente.telefone, cliente.cidade)
            )

    def limpa_tela(self):
        self.codigo_entry.delete('0', tk.END)
        self.nome_entry.delete('0', tk.END)
        self.tel_entry.delete('0', tk.END)
        self.city_entry.delete('0', tk.END)

    def OnDoubledClick(self, event):
        self.limpa_tela()
        self.listacli.selection()
        for n in self.listacli.selection():
            col1, col2, col3, col4 = self.listacli.item(n, 'values')
            self.codigo_entry.insert(tk.END, col1)
            self.nome_entry.insert(tk.END, col2)
            self.tel_entry.insert(tk.END, col3)
            self.city_entry.insert(tk.END,col4)



class Cliente(Base):
            __tablename__ = "Clientes"
            codigo = Column("codigo", Integer, primary_key = True, autoincrement = True)
            nome = Column("nome", String)
            telefone = Column("telefone", String)
            cidade = Column("cidade", String)

            def __init__(self, nome, telefone, cidade):
                self.nome = nome
                self.telefone = telefone
                self.cidade = cidade