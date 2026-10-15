# livro_flask

Projeto inicial de uma aplicação web em Flask para gerenciamento de produtos. O código contém modelos de usuário, papel, categoria e produto, além de uma estrutura inicial para a área administrativa e recuperação de senha.

> **Estado do projeto:** a aplicação ainda está em desenvolvimento. No estado atual, a rota `/` retorna apenas `Hello World!`; controladores, telas, migração e arquivo SQL estão vazios. A configuração também precisa de um ajuste antes que o servidor possa ser iniciado (detalhes abaixo).

## Tecnologias

- Python
- Flask
- Flask-SQLAlchemy
- MySQL, usando o driver `mysqlclient` (`mysql+mysqldb`)

O repositório não contém um arquivo de dependências (`requirements.txt` ou `pyproject.toml`). As dependências acima foram identificadas nos imports e na URI do banco de dados existentes no código.

## Estrutura

```text
.
├── admin/                 # Área administrativa (módulos ainda vazios)
├── controller/            # Controladores de usuário, produto e e-mail (vazios)
├── model/                 # Modelos SQLAlchemy: User, Role, Category e Product
├── static/css/            # Folhas de estilo (vazias)
├── templates/             # Templates de login, recuperação e administração (vazios)
├── app.py                 # Factory Flask e rota inicial
├── config.py              # Configurações de ambiente e URI do banco
├── run.py                 # Inicialização do servidor
├── migrate.py             # Reservado para migrações (vazio)
├── livro_flask.sql        # Reservado para o esquema SQL (vazio)
└── json.json              # Exemplo/documentação dos campos de produto
```

## Modelos disponíveis

- **User:** nome de usuário, e-mail, senha, datas de criação/atualização, código de recuperação, estado ativo e referência a um papel.
- **Role:** nome do papel.
- **Category:** nome e descrição da categoria.
- **Product:** nome, descrição, quantidade, imagem, preço, datas, estado, usuário criador e categoria.

Os modelos estão definidos, mas não há rotas ou controladores implementando operações de cadastro, consulta, edição ou remoção.

## Preparação do ambiente

Requer Python e um servidor MySQL acessível. Crie e ative um ambiente virtual na raiz do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as bibliotecas identificadas no código:

```bash
pip install Flask Flask-SQLAlchemy mysqlclient
```

Em sistemas Linux, a instalação de `mysqlclient` pode exigir os headers e ferramentas de desenvolvimento do MySQL/MariaDB fornecidos pela distribuição.

## Configuração do banco

Edite `config.py` e substitua a URI de exemplo pelos dados do seu banco MySQL:

```text
mysql+mysqldb://USUARIO:SENHA@HOST:3306/NOME_DO_BANCO
```

Crie previamente o banco de dados e configure as credenciais apropriadas. A URI atual contém valores ilustrativos (`user`, `passwd`, `host`, `port` e `database`) e não conecta a um banco real. Não use credenciais reais em arquivos versionados; para um ambiente compartilhado, mova segredos para variáveis de ambiente.

## Inicialização

O ponto de entrada previsto é `run.py`. A configuração selecionada é determinada por `FLASK_ENV`, com os nomes `development`, `testing` ou `production`. Por exemplo, após corrigir o bloqueio descrito abaixo:

```bash
export FLASK_ENV=development
python run.py
```

O perfil de desenvolvimento está configurado para usar `localhost:8000`. Atualmente, não há comandos de criação de tabelas ou migração implementados; `migrate.py` e `livro_flask.sql` estão vazios.

## Bloqueio conhecido para execução

`app.py`, `run.py` e os módulos de modelo importam `app_config` e `app_active` diretamente de `config.py`. Porém, essas variáveis estão indentadas dentro da classe `ProductionConfig`, não no escopo do módulo. Assim, os imports falham antes de o servidor iniciar.

Antes de executar, mova `app_config` e `app_active` para o escopo do módulo em `config.py` e confirme também que `FLASK_ENV` está definido para uma das chaves disponíveis (`development`, `testing` ou `production`). A configuração atual ainda usa uma chave secreta fixa de exemplo; ela deve ser substituída e mantida fora do controle de versão antes de qualquer uso real.

## Próximos passos sugeridos

1. Corrigir e externalizar a configuração de ambiente e os segredos.
2. Definir dependências e versões em `requirements.txt` ou `pyproject.toml`.
3. Implementar inicialização do banco e migrações.
4. Criar rotas, controladores, templates e testes para os fluxos de usuário e produtos.
