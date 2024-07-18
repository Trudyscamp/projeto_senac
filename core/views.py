from django.shortcuts import render

def index(request):
    conteudos = {
        'curso' : 'Programação em Python - Django Framework'
    }
    return render(request, 'index.html', conteudos)
def contato(request):
    return render(request, 'contato.html')
