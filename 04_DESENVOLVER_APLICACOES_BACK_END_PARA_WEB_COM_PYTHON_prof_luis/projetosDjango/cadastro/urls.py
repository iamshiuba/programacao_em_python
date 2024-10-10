from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segundo', views.segundo, name='segundo'),

    path('pagina', views.pagina, name='pagina'),

    path('mensagem', views.mensagem, name='mensagem'),

    #Cursos
    path('listarcursos', views.listarcursos, name='listarcursos'),

    path('alterarcurso/<int:codigo>', views.alterarcurso, name='alterarcurso'),

    path('incluircurso', views.incluircurso, name='incluircurso'),

    #Alunos
    path('listaralunos', views.listaralunos, name='listaralunos'),
    
    path('incluiraluno', views.incluiraluno, name='incluiraluno'),

    #Professores
    path('listarprofessores', views.listarprofessores, name='listarprofessores'),

    path('incluirprofessor', views.incluirprofessor, name='incluirprofessor'),
]