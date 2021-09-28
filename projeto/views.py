from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'cursos.html')

def projetos(request):
    return render(request, 'projetos.html')

def sobre(request):
    return render(request, 'sobre.html')
