from django.contrib import admin
from django.urls import path
from alunos import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('informacao', views.informacao_aluno, name="informacao"),
]
