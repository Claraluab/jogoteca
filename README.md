 Jogoteca (Aplicação Web Flask)
📝 Descrição
A Jogoteca é uma aplicação web desenvolvida com Flask (Python) para gerenciar uma coleção de jogos. Permite cadastrar, editar, visualizar e deletar jogos, com um sistema seguro de autenticação de usuários.

✨ Funcionalidades
✅ Cadastro, login e logout de usuários com segurança

✅ CRUD completo de jogos (Create, Read, Update, Delete)

✅ Upload de capas para os jogos

✅ Validação de formulários robusta

✅ Interface responsiva com Bootstrap

✅ Sistema de hash seguro para senhas usando Flask-Bcrypt

🔒 Segurança
Todas as senhas são armazenadas de forma criptografada usando Flask-Bcrypt

Sistema de autenticação seguro com sessões

Proteção contra ataques CSRF nos formulários

Validação de entrada de dados em todos os formulários

🛠 Tecnologias Utilizadas
Backend: Python com Flask

Frontend: HTML, CSS, Bootstrap

Banco de Dados: MySQL (com SQLAlchemy ORM)

Autenticação Segura: Flask-Bcrypt para hash de senhas

Gerenciamento de Formulários: Flask-WTF com CSRF protection

⚙️ Configuração do Ambiente
Pré-requisitos
Python 3.8+

MySQL Server instalado e rodando

pip (gerenciador de pacotes Python)

Instalação
Clone o repositório:

bash
git clone https://github.com/seu-usuario/jogoteca.git
cd jogoteca
Crie um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
pip install -r requirements.txt
Configure o banco de dados MySQL:

Crie um banco de dados MySQL

Configure as variáveis de conexão no arquivo de configuração do Flask

Execute as migrações do banco de dados:

bash
flask db init
flask db migrate
flask db upgrade
Executando a Aplicação
bash
flask run
Acesse no navegador: http://localhost:5000

🗂 Estrutura do Projeto
text
jogoteca/
├── app.py                # Aplicação principal Flask
├── models.py             # Modelos de banco de dados MySQL
├── helpers.py            # Funções auxiliares e formulários
├── static/               # Arquivos estáticos (CSS, JS)
├── templates/            # Templates HTML
│   ├── base.html         # Template base
│   ├── lista.html        # Lista de jogos
│   ├── novo.html         # Formulário de novo jogo
│   ├── editar.html       # Formulário de edição
│   ├── login.html        # Página de login
│   └── cadastro.html     # Página de cadastro
├── uploads/              # Armazena as capas dos jogos
├── migrations/           # Migrações do banco de dados
└── requirements.txt      # Dependências do projeto
📌 Rotas Principais
Rota	Método	Descrição
/	GET	Lista todos os jogos
/novo	GET	Formulário para adicionar novo jogo (requer autenticação)
/criar	POST	Processa o formulário de novo jogo
/editar/<id>	GET	Formulário para editar jogo (requer autenticação)
/atualizar	POST	Processa o formulário de edição
/deletar/<id>	GET	Remove um jogo (requer autenticação)
/login	GET	Página de login
/autenticar	POST	Processa o login
/logout	GET	Faz logout
/cadastro	GET/POST	Página de cadastro de novos usuários
👤 Primeiro Acesso
Acesse a rota /cadastro para criar seu primeiro usuário

Faça login com as credenciais criadas

Comece a gerenciar sua coleção de jogos

