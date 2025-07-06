# Projeto de Banco de Dados - Gestão do Restaurante Universitário (UnB)

Projeto desenvolvido para a disciplina de Banco de Dados da Universidade de Brasília (UnB). O sistema consiste em um banco de dados construído com Django e PostgreSQL para gerenciar as operações de um Restaurante Universitário, incluindo o controle de cardápios, pratos, clientes, fornecedores e transações.

## Tecnologias Utilizadas
* **Backend:** Python 3, Django 4+
* **Banco de Dados:** PostgreSQL
* **Frontend:** HTML, CSS (via templates do Django)
* **Controle de Versão:** Git e GitHub

---

## Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados na sua máquina:
* [Python 3.10+](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)
* [Git](https://git-scm.com/downloads/)

---

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento após clonar o projeto.

**1. Clone o Repositório**
```bash
git clone [https://github.com/AleCLJunq/TrabalhoBD.git](https://github.com/AleCLJunq/TrabalhoBD.git)
cd TrabalhoBD
```

**2. Crie e Ative o Ambiente Virtual**
```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
```

**3. Instale as Dependências**
O arquivo `requirements.txt` contém todos os pacotes Python necessários.
```bash
pip install -r requirements.txt
```

**4. Configure o Banco de Dados**
Conecte-se ao seu servidor PostgreSQL (usando o `psql` ou pgAdmin) e crie o banco de dados para o projeto.
```sql
CREATE DATABASE ru_unb;
```

**5. Configure as Variáveis de Ambiente**
Este projeto usa um arquivo `.env` para gerenciar segredos e configurações.
```bash
# Copie o arquivo de exemplo para criar seu próprio arquivo .env
# No Windows:
copy .env.example .env
# No Linux/macOS:
cp .env.example .env
```
Após copiar, **abra o arquivo `.env`** e preencha as variáveis com seus dados (SECRET_KEY, DB_USER, DB_PASSWORD, etc.).

**6. Aplique as Migrações do Banco**
Este comando irá criar todas as tabelas do projeto no seu banco de dados.
```bash
python manage.py migrate
```

**7. Crie um Superusuário**
Você precisará de um usuário administrador para acessar o painel do Django Admin.
```bash
python manage.py createsuperuser
```
Siga as instruções para criar seu usuário e senha.

**8. (Opcional) Popule o Banco com Dados Iniciais**
Para ter dados de teste, execute o script de população.
```bash
python populate_db.py
```

---

## Executando o Projeto

Com tudo configurado, inicie o servidor de desenvolvimento do Django:
```bash
python manage.py runserver
```

A aplicação estará disponível nos seguintes endereços:
* **Interface Pública (Lista de Restaurantes):** `http://127.0.0.1:8000/restaurantes/`
* **Painel de Administração (CRUD):** `http://127.0.0.1:8000/admin/`

## Autores
* [Alexandre Junqueira]
* [Rodrigo Rafik]