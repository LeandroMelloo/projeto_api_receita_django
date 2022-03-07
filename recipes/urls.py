from django.urls import path

from recipes.views import about, contact, home

urlpatterns = [
    path('', home),  # dominio/recipes/
    path('contact/', contact),  # dominio/recipes/contact/
    path('about/', about),  # dominio/recipes/about/
]
