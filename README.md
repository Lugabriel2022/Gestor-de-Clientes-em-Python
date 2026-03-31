📋 Sistema de Gestão de Clientes (CRUD)
Este é um sistema desktop para gerenciamento de registros de clientes, desenvolvido em Python. O projeto foca em aplicar conceitos de Mapeamento Objeto-Relacional (ORM) e automação de documentos para facilitar o fluxo de trabalho administrativo.

🚀 Funcionalidades
Ciclo CRUD Completo: Criação, leitura, atualização e exclusão de registros de clientes.

Persistência de Dados: Uso de banco de dados local para armazenamento seguro das informações.

Interface Interativa: Tabela dinâmica (Treeview) com suporte a clique duplo para edição rápida.

Relatórios em PDF: Geração automática de fichas de clientes formatadas para impressão.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Interface Gráfica: Tkinter (Customização de widgets e eventos)

Banco de Dados & ORM: SQLAlchemy com SQLite3

Gerador de PDF: ReportLab

Navegação: Webbrowser (Para visualização imediata de relatórios)

📂 Estrutura do Projeto
```
CRUD/
├── Main.py          # Ponto de entrada e interface principal
├── Utils.py         # Lógica de negócio, classes do banco e funções CRUD
├── Report.py        # Módulo especializado em geração de PDFs
└── clientes.db      # Banco de dados SQLite (gerado automaticamente)


⚙️ Como Executar
1. Clone o repositório:

	git clone https://github.com/seu-usuario/nome-do-repo.git
	cd nome-do-repo
	
2. Instale as dependências:
	pip install sqlalchemy reportlab

3. inicie a aplicação:
	python3 Main.py

💡 Destaques Técnicos
Arquitetura Modular: Separação clara entre a construção da interface (Main.py), a lógica de dados (Utils.py) e o serviço de impressão (Report.py), facilitando a manutenção.

SQLAlchemy: Implementação de classes para representar tabelas, garantindo que o código seja escalável para outros bancos de dados como PostgreSQL ou MySQL com poucas alterações.
