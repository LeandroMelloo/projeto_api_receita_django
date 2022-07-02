# projeto_api_receita_django
Projeto API de receita com Django Rest Framework, Docker, PostgreSQL e TDD

# Comando Docker
docker build .
docker-compose build
docker-compose run app sh -c "django-admin.py startproject core ."
docker-compose run app sh -c "python manage.py startapp main"
docker-compose run app sh -c "python manage.py makemigrations main"

docker-compose run app sh -c "python manage.py test"
docker-compose run app sh -c "python manage.py test && flake8"

docker-compose build
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose up

# Dockerfile
O Dockerfile é usado para construir nossa imagem, que contém um mini sistema operacional Linux com todas as dependências necessárias para rodar nosso projeto.

# Linting
Isso mesmo! Linting é usado para garantir que o código seja formatado corretamente. Ele destaca problemas como espaçamento de tabulação e comprimentos de linha inválidos.

# GitHub Actions
- Ferramenta de automação para CI/CD
- Ferramenta similar ao Travis-CI, GitLab CI/CD, Jenkins
- Simplificando, permite que você execute tarefas sempre que seu código for alterado
- Permite automatizar determinadas tarefas

# Docker Hub
- O Docker Hub é uma plataforma que permite extrair imagens de base do Docker para sua máquina local

# Configuração Docker Hub e Git Hub
- Token e Username para logar no Docker Hub deve ser inserido no Github