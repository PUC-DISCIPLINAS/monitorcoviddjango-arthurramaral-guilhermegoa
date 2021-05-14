# Trabalho - Django MVC/MTV

## Alunos

[Arthur Rocha Amaral](https://github.com/ArthurRAmaral)

[Guilherme Oliveira Antônio](https://github.com/guilhermegoa)

---

## Professor

Hugo Bastos De Paula

---

## Descrição

Neste trabalho, deverá ser desenvolvido um sistema pequeno dashboard (pode ser no formato de tabela), que irá exibir uma tabela de infecção dos países por COVID-19. A tabela deve ter os seguintes campos:

|CAMPO |FORMATO|
|------|-------|
|país|String|
|casos_confirmados|Inteiro|
|mortes|Inteiro|
|recuperados|Inteiro|

O aplicativo deve autenticar o usuário admin, e apenas o admin, poderá cadastrar ou editar novos dados. A tabela de consulta é pública.

Resumo dos requisitos:

- O sistema deve possuir um usuário admin.
- O sistema deve possuir um model que armazenará os dados do COVID-19 e um model que armazena os nomes dos países.
- O sistema deve possuir um CRUD simples para os dados do COVID-19.
- O cadastro dos dados deve possuir um combo box que carrega os dados do model de países.
- Apenas o usuário admin poderá cadastrar dados na tabela do COVID-19.
- Os dados da tabela devem ser exibidos na página principal, aberta e pública para qualquer usuário sem a necessidade de login.
- Deverá ser criado um layout para a tabela.

---

## Pré-requisitos

- python3
- pip
- django

## Como usar

### Instalar requisitos

```sh
pip install requiriments.txt
```

### Iniciar aplicação:

```sh
python manage.py runserver
```
- Link da aplicação [http://127.0.0.1:8000]

Para entrar na parte administrativa do site

- Link do admin [http://127.0.0.1:8000/admin]
- login: admin
- senha: admin
