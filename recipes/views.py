from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home/home.html', context={
        'name': 'Leandro Mello'
    })


def contact(request):
    return render(request, 'recipes/contact/contact.html', context={
        'phone': '(11)97673-0968'
    })


def about(request):
    return HttpResponse('<h1>Sobre</h1>')
