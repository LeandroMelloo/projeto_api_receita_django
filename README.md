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