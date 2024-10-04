from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segundo', views.segundo, name='segundo'),

    path('pagina', views.pagina, name='pagina'),

    path('mensagem', views.mensagem, name='mensagem'),

    #Cursos
    path('listarcursos', views.listarcursos, name='listarcursos'),
    #Alunos
    path('listaralunos', views.listaralunos, name='listaralunos'),
    #Professores
    path('listarprofessores', views.listarprofessores, name='listarprofessores'),
]