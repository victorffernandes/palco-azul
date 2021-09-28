
def turmas(request):
    from alunos.models import Turma
    return {'turmas': list(Turma.objects.values())}