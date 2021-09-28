from django.contrib import admin
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre', views.sobre, name="sobre"),
    path('admin/', admin.site.urls, name="admin"),
    path('cursos', views.cursos, name="cursos"),
    path('projetos', views.projetos, name="projetos"),
    path('alunos/', include('alunos.urls'), name="alunos"),
    path('autenticacao/', include('autenticacao.urls'), name="autenticaco")
]
