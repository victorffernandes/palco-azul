from django.contrib import admin

# Register your models here.
from .models import Aluno, Atividade, Turma
 
admin.site.register(Aluno)
admin.site.register(Atividade)
admin.site.register(Turma)