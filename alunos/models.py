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
    picture = models.FileField(upload_to='static/picture/',blank=True)

    class Meta:
        db_table='Alunos'
        ordering=('nome', )

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    cpfAluno = models.CharField(max_length=60)
    descricao = models.CharField(max_length=60)
    entregue = models.BooleanField()
    link = models.FileField(upload_to='static/pdf/',blank=True)

    class Meta:
        db_table='Atividade'
        ordering=('descricao', )

    def __str__(self):
        return self.descricao

class Turma(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=300)
    image = models.FileField(upload_to='static/turmas/')

    class Meta:
        db_table='Turma'
        ordering=('nome', )

    def __str__(self):
        return self.nome
