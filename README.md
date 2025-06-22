# 🎮 Jogoteca - Sistema de Gerenciamento de Jogos

![Flask](https://img.shields.io/badge/Flask-2.3.2-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)

## 📋 Descrição

Aplicação web em Flask para gerenciar sua coleção de jogos, com sistema de cadastro e autenticação seguros, upload de capas, e CRUD completo de jogos.

## ✨ Features

- ✔️ Cadastro e autenticação segura de usuários com senha criptografada  
- ✔️ CRUD completo de jogos (criar, listar, editar, deletar)  
- ✔️ Upload e gerenciamento de capas dos jogos  
- ✔️ Interface responsiva com Bootstrap 5  
- ✔️ Banco de dados MySQL usando SQLAlchemy ORM  
- ✔️ Proteção contra CSRF em todos os formulários  
- ✔️ Validação de dados de entrada  

## 🛠️ Tecnologias Utilizadas

| Tecnologia    | Finalidade                        |
|--------------|----------------------------------|
| Flask        | Backend principal                 |
| Flask-WTF    | Formulários e validação           |
| Flask-Bcrypt | Hash de senhas                   |
| MySQL        | Banco de dados                   |
| SQLAlchemy   | ORM para MySQL                  |
| Bootstrap 5  | Frontend responsivo              |

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior  
- MySQL Server instalado  
- Git instalado  

### Configuração do Ambiente

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Inicializar e Aplicar Migrações do Banco
```bash
flask db init
flask db migrate -m "Inicializando banco de dados"
flask db upgrade
```

### Executar a Aplicação
```bash
flask run
```
```markdown
Abra o navegador e acesse: http://localhost:5000
```
## 🔒 Segurança
- Senhas armazenadas com hash BCrypt, garantindo segurança
- Proteção CSRF ativa para todos os formulários
- Validação de dados de entrada para evitar inconsistências e ataques





