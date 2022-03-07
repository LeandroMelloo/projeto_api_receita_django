from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home/home.html', context={
        'name': 'Leandro Mello'
    })


def contact(request):
    return HttpResponse('<h1>Contato</h1>')


def about(request):
    return HttpResponse('<h1>Sobre</h1>')
