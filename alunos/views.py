from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from alunos.models import Aluno, Atividade, Turma
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@login_required(login_url='/autenticacao/login')
def dashboard(request):
    current_user = request.user
    try:
        aluno = Aluno.objects.get(email=current_user.email)
    except ObjectDoesNotExist as not_exists_error:
        return render(request, 'alunos/aluno_nao_existente.html')

    colegas_classe = Aluno.objects.filter(sala=aluno.sala,turma=aluno.turma)
    aluno_atividades = Atividade.objects.filter(cpfAluno=aluno.cpf)
    return render(request, 'alunos/dashboard.html', {'colegas_classe': colegas_classe, 'aluno': aluno, 'aluno_atividades': aluno_atividades})


@login_required(login_url='/autenticacao/login')
def informacao_aluno(request):
    current_user = request.user
    try:
        aluno = Aluno.objects.get(email=current_user.email)
    except ObjectDoesNotExist as not_exists_error:
        return render(request, 'alunos/aluno_nao_existente.html')

    return render(request, 'alunos/informacao.html', {'aluno': aluno})

def turmas(request):
    turmas = list(Turma.objects.values())
    return JsonResponse(turmas,safe=False)
