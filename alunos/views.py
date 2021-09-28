from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/autenticacao/login')
def dashboard(request):
    current_user = request.user
    print(current_user.email)
    return render(request, 'alunos/dashboard.html')

@login_required(login_url='/autenticacao/login')
def informacao_aluno(request):
    return render(request, 'alunos/informacao.html')


