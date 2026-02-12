from django.shortcuts import render
from .models import Protudo

def index(request):
    context = {'curso': 'Desenvolvimento de sistema'}
    return render(request, 'index.html', context)

def contato(request):
    context = {
        'nome': 'joel Matos',
        'telefone': 'aaa',
        'email': 'aa'
    }
    return render(request, 'contato.html',context)

def produtos(request):
    produtos = Protudo.objects.all()
    context = {'prod': produtos}
    return render(request, 'produtos.html', context)