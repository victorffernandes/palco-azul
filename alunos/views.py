from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from alunos.models import Aluno
# Create your views here.

@login_required(login_url='/autenticacao/login')
def dashboard(request):
    current_user = request.user
    aluno = Aluno.objects.get(email=current_user.email)
    colegas_classe = Aluno.objects.filter(sala=aluno.sala)
    print(colegas_classe)
    return render(request, 'alunos/dashboard.html')

@login_required(login_url='/autenticacao/login')
def informacao_aluno(request):
    current_user = request.user
    aluno = Aluno.objects.get(email=current_user.email)
    print(aluno)
    return render(request, 'alunos/informacao.html', { aluno: aluno })


