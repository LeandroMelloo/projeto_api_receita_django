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