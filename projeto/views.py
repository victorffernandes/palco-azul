from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'frase': frase})

def cursos(request):
    return render(request, 'cursos.html')

def projetos(request):
    return render(request, 'projetos.html')

def sobre(request):
    return render(request, 'sobre.html')
