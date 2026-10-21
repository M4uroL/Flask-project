# Flask Project

Projeto inicial em Flask para gerenciamento de usuários, categorias e produtos, com estrutura de autenticação, administração via Flask-Admin e integração com MySQL.

Este repositório está em desenvolvimento e foi organizado para servir como base de estudo e evolução de uma aplicação web com arquitetura MVC-lite, modelos SQLAlchemy e rotas específicas para autenticação e CRUD de produtos.

## Visão geral

A aplicação foi pensada como um sistema simples de gestão de estoque, com foco em:

- gerenciamento de usuários e papéis
- cadastro de categorias
- cadastro e atualização de produtos
- painel administrativo com Flask-Admin
- autenticação e recuperação de senha
- integração com banco MySQL usando SQLAlchemy

## Stack tecnológica

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Admin
- MySQL + mysqlclient
- passlib

## Estrutura do projeto

```text
.
├── admin/
│   ├── Admin.py          # Configuração do painel administrativo
│   └── Views.py          # Views personalizadas do Flask-Admin
├── controller/
│   ├── Product.py        # Controller de produtos
│   ├── User.py           # Controller de usuários/autenticação
│   └── Email.py          # Arquivo reservado para envio de e-mail
├── model/
│   ├── Category.py       # Modelo de categoria
│   ├── Product.py        # Modelo de produto
│   ├── Role.py           # Modelo de papel/role
│   └── User.py           # Modelo de usuário
├── static/
│   └── css/              # Arquivos de estilo do projeto
├── templates/
│   └── ...               # Templates de login, recuperação e administração
├── app.py                # Criação da aplicação Flask e rotas principais
├── config.py             # Configurações globais do projeto e ambientes
├── run.py                # Inicialização da aplicação
├── migrate.py            # Arquivo reservado para migração/DDL
├── livro_flask.sql       # Arquivo reservado para schema SQL
├── json.json             # Exemplo de payload de dados de produto
├── README.md             # Documentação do projeto
└── requirements.txt      # Ainda não existe (pendente)
```

## Modelos principais

### User

Representa o usuário do sistema e inclui:

- `id`
- `username`
- `email`
- `password`
- `date_created`
- `last_update`
- `recovery_code`
- `active`
- `role` (FK para `Role`)
- relacionamento com `Role`

Além disso, o modelo implementa:

- hash de senha com `pbkdf2_sha256`
- método `set_password()`
- método `verify_password()`

### Role

Representa a função de cada usuário, como administrador ou cliente. Possui:

- `id`
- `name`

### Category

Modela as categorias dos produtos:

- `id`
- `name`
- `description`

### Product

Modela o registro de produtos do sistema:

- `id`
- `name`
- `description`
- `qtd`
- `image`
- `price`
- `date_created`
- `last_update`
- `status`
- `user_created` (FK para `User`)
- `category` (FK para `Category`)

## Painel administrativo

O projeto usa Flask-Admin para expor e gerenciar dados no painel administrativo.

A configuração em `admin/Admin.py` define:

- nome do admin: `Meu Estoque`
- grupos de menu para usuários e produtos
- views para `Role`, `User`, `Category` e `Product`
- link de logout

Também há uma `HomeView` personalizada em `admin/Views.py`, com uma landing page para o painel administrativo.

## Rotas implementadas

A aplicação define as seguintes rotas principais em `app.py`:

- `GET /login/` — tela de login
- `POST /login/` — autenticação do usuário
- `GET /recovery-password/` — recuperação de senha
- `POST /recovery-password/` — envio de e-mail de recuperação
- `GET /profile/<int:id>/action/<action>/` — ações de perfil
- `POST /profile` — criação de perfil
- `PUT /profile/<int:id>` — edição completa de perfil
- `POST /product` — cadastro de produto
- `PUT /product` — atualização de produto

## Configuração e ambiente

O projeto usa `config.py` para gerenciar os ambientes:

- `development`
- `testing`
- `production`

A classe base define:

- `SECRET`
- `SQLALCHEMY_DATABASE_URI`
- `TEMPLATE_FOLDER`
- `ROOT_DIR`

No arquivo atual, a URI do banco está em formato de exemplo:

```python
mysql+mysqldb://user:passwd@host:port/database
```

Você deve substituir por dados reais do seu banco MySQL antes de rodar a aplicação.

## Requisitos do ambiente

Certifique-se de ter instalado:

- Python 3
- MySQL acessível localmente ou remotamente
- bibliotecas do projeto

## Instalação

Crie um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências principais:

```bash
pip install Flask Flask-SQLAlchemy flask-admin mysqlclient passlib
```

Observação: em distribuições Linux, a instalação de `mysqlclient` pode exigir bibliotecas e headers do MySQL/MariaDB, como `libmysqlclient-dev` ou equivalentes.

## Execução

O ponto de entrada do projeto é `run.py`.

```bash
export FLASK_ENV=development
python run.py
```

No ambiente de desenvolvimento, a aplicação é configurada para rodar em:

- host: `localhost`
- porta: `8000`

## Banco de dados

O projeto utiliza SQLAlchemy com MySQL e já prepara a estrutura de modelos para integração com banco relacional.

Ainda é necessário:

- criar o banco de dados manualmente
- configurar a `SQLALCHEMY_DATABASE_URI`
- criar as tabelas via migração ou script SQL

## Status atual do projeto

O projeto está em fase inicial de desenvolvimento. A estrutura base já existe e alguns elementos importantes foram implementados, mas ainda há pendências relevantes:

- `requirements.txt` ainda não foi criado
- `migrate.py` está vazio
- `livro_flask.sql` está vazio
- rotas de autenticação e recuperação ainda precisam ser finalizadas
- controllers de usuário e e-mail ainda têm trechos incompletos
- os templates e arquivos estáticos ainda não possuem implementação completa
- parte da configuração precisa ser externalizada e padronizada para uso em produção

## Próximos passos sugeridos

1. criar arquivo `requirements.txt` com versões fixas
2. configurar variáveis de ambiente para banco e segredo
3. implementar migrações do banco
4. finalizar autenticação de usuários
5. completar CRUD de produtos e usuários
6. criar templates HTML e estilos visuais
7. adicionar testes automatizados
8. separar melhor a responsabilidade entre modelos, controllers e views

## Observações importantes

O projeto ainda não está pronto para uso em produção, mas já possui uma base sólida para desenvolvimento incremental. A estrutura atual demonstra uma aplicação Flask com organização por módulos, uso de SQLAlchemy e painel administrativo com Flask-Admin.

Se você quiser, posso continuar e te ajudar a:

- criar um `requirements.txt`
- escrever o `livro_flask.sql`
- ajustar `config.py` para uso com variáveis de ambiente
- implementar a autenticação e o CRUD completo
- gerar um README mais profissional com badges, screenshots e instruções detalhadas
