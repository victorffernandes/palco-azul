from django.db import models

# Create your models here.
from django.db import models
class Aluno(models.Model):
    nome = models.CharField(max_length=60)
    turma = models.CharField(max_length=60)
    sala = models.CharField(max_length=60)
    idade = models.IntegerField(max_length=5)
    cpf = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=60)

    class Meta:
        db_table='Alunos'
        ordering=('nome', )

    def __str__(self):
        return self.nome
