from django.contrib import admin
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre', views.sobre, name="sobre"),
    path('admin', admin.site.urls, name="admin"),
    path('cursos', views.cursos, name="cursos"),
    path('projetos', views.projetos, name="projetos")
]

#     Como acessar a página index.html do projeto:
#     http://127.0.0.1:8000/
#
#     Como acessar a página index.html de produto:
#     http://127.0.0.1:8000/produto/