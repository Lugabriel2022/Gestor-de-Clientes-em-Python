# Importa as ferramentas do ReportLab para gerar PDFs
from reportlab.pdfgen import canvas              # módulo principal para desenhar no PDF
from reportlab.lib.pagesizes import letter, A4   # tamanhos de página prontos (Letter, A4)
from reportlab.pdfbase import pdfmetrics         # gerenciar fontes
from reportlab.pdfbase.ttfonts import TTFont     # registrar fontes TrueType
from reportlab.platypus import SimpleDocTemplate, Image  # estruturas mais avançadas (não usadas aqui)
import webbrowser as web                         # abrir o PDF no navegador


class Relatórios():
    # Função para abrir o PDF gerado
    def printCliente(self):
        web.open("cliente.pdf")  # abre o arquivo no navegador padrão

    # Função principal que gera o relatório do cliente
    def gerarRelatCliente(self):
        # Cria um novo PDF chamado "cliente.pdf"
        self.client = canvas.Canvas("cliente.pdf")
        
        # Pega os dados digitados nos campos da interface Tkinter
        self.codigo = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.foneRel = self.tel_entry.get()
        self.cidadeRel = self.city_entry.get()

        # Define a fonte e escreve o título
        self.client.setFont("Helvetica-Bold", 24)
        self.client.drawString(200, 790, 'Ficha do Cliente')  
        # drawString(x, y, texto) → escreve o texto na posição (x,y)
        # coordenadas começam no canto inferior esquerdo da página

        # Escreve os rótulos dos campos
        self.client.setFont("Helvetica-Bold", 18)
        self.client.drawString(58, 700, 'Codigo: ')
        self.client.drawString(58, 670, 'Nome: ')
        self.client.drawString(58, 630, 'Telefone: ')
        self.client.drawString(58, 600, 'Cidade: ')

        # Escreve os valores digitados pelo usuário
        self.client.setFont("Helvetica", 18)
        self.client.drawString(150, 700, self.codigo)
        self.client.drawString(150, 670, self.nomeRel)
        self.client.drawString(150, 630, self.foneRel)
        self.client.drawString(150, 600, self.cidadeRel)

        # Desenha retângulos para dar estilo ao relatório
        self.client.rect(20, 550, 550, 200, fill = False, stroke = True)
        self.client.rect(30, 560, 530, 180, fill = False, stroke = True)
        # rect(x, y, largura, altura) → desenha um retângulo

        # Finaliza a página e salva o PDF
        self.client.showPage()  # cria uma nova página (a atual é "fechada")
        self.client.save()      # salva o arquivo em disco
        self.printCliente()     # abre o PDF gerado
