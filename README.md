# Loan Management System

Este projeto é uma aplicação Django para gerenciar propostas de empréstimos.

## Estrutura do projeto

    📦loan_managment
    ┣ 📂loan_management
     ┃ ┣ 📂loan_management
     ┃ ┃ ┣ 📜asgi.py
     ┃ ┃ ┣ 📜celery.py
     ┃ ┃ ┣ 📜settings.py
     ┃ ┃ ┣ 📜urls.py
     ┃ ┃ ┣ 📜wsgi.py
     ┃ ┃ ┗ 📜__init__.py
     ┃ ┣ 📂proposals
     ┃ ┃ ┣ 📂migrations
     ┃ ┃ ┃ ┣ 📜0001_initial.py
     ┃ ┃ ┃ ┣ 📜0002_alter_proposal_cpf.py
     ┃ ┃ ┃ ┣ 📜0003_alter_proposal_cpf.py
     ┃ ┃ ┃ ┣ 📜0004_alter_proposal_cpf.py
     ┃ ┃ ┃ ┣ 📜0005_alter_proposal_status.py
     ┃ ┃ ┃ ┗ 📜__init__.py
     ┃ ┃ ┣ 📂static
     ┃ ┃ ┣ 📂tests
     ┃ ┃ ┃ ┗ 📜test_proposals.py
     ┃ ┃ ┣ 📜admin.py
     ┃ ┃ ┣ 📜apps.py
     ┃ ┃ ┣ 📜models.py
     ┃ ┃ ┣ 📜serializers.py
     ┃ ┃ ┣ 📜services.py
     ┃ ┃ ┣ 📜tasks.py
     ┃ ┃ ┣ 📜tests.py
     ┃ ┃ ┣ 📜urls.py
     ┃ ┃ ┣ 📜views.py
     ┃ ┃ ┗ 📜__init__.py
     ┃ ┣ 📜create_superuser.py
     ┃ ┣ 📜db.sqlite3
     ┃ ┣ 📜manage.py
     ┃ ┗ 📜__init__.py
     ┣ 📜.env-example
     ┣ 📜docker-compose.yaml
     ┣ 📜Dockerfile
     ┣ 📜README.md
     ┗ 📜requirements.txt

## Instalação

1. Primeiro, clone o repositório do projeto.

`git clone <URL do repositório>`

2. Construa e execute o projeto com Docker Compose.

`docker-compose up --build -d`

## Uso

Você pode enviar propostas de empréstimos e ver a decisão do sistema (APROVADA/NEGADA) acessando `http://localhost:8000/api/proposals/`. A decisão é tomada usando um algoritmo de randomização que conforme o número de vezes(se par/ímpar) recebe APROVADA/NEGADA.

## Sobre

Este projeto inclui um módulo `proposals` que gerencia propostas de empréstimos. Ele inclui um `ProposalViewSet` para interação via API, e uma view `proposal_form_view` que apresenta um formulário HTML para submissão de novas propostas.

## Docker

Este projeto usa Docker e Docker Compose para simplificar o processo de desenvolvimento e implantação. O serviço `django` no arquivo `docker-compose.yaml` é responsável por executar o servidor de desenvolvimento Django, enquanto o serviço `celery` executa o worker Celery. Ambos os serviços dependem do RabbitMQ como um broker de mensagens, que é provido pelo serviço `rabbitmq`.

## Celery

Este projeto usa o Celery para tarefas assíncronas. As configurações do Celery estão no arquivo `celery.py`.

## Considerações

1. Criação Dinâmica de Campos no Django Admin

A capacidade de criar campos dinamicamente no Django admin é complexa e não é um recurso padrão do Django. Implementar essa funcionalidade pode adicionar uma camada significativa de complexidade ao projeto, além de possíveis problemas com gerenciamento de banco de dados e permissões de usuário. O Django puro pode não ser a ferramenta mais apropriada para essa tarefa.

Se a criação dinâmica de campos é um requisito essencial, pode ser mais apropriado considerar o uso de um sistema de gerenciamento de conteúdo (CMS) mais robusto, como o Django CMS. Estes frameworks são projetados para fornecer maior flexibilidade na definição da estrutura de dados e permitem que os administradores configurem campos personalizados através da interface do usuário.

No entanto, o escopo deste projeto sugere o uso de campos específicos. Portanto, preferi aderir ao uso de campos padrão no Django, conforme listado a seguir:

- Nome Completo

- CPF

- Endereço

- Valor do Empréstimo Pretendido

Estes campos são mais do que suficientes para cumprir os requisitos do projeto e a implementação é significativamente simplificada em comparação com a criação dinâmica de campos.

## Testes

Criei testes unitários com as ferramentas do próprio django e podem ser encontrados em `loan_management\proposals\tests\test_proposals.py`
