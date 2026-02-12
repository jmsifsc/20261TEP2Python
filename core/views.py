from django.shortcuts import render

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
    return render(request, 'produtos.html')