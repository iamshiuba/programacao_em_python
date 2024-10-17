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

    path('excluircurso/<int:codigo>', views.excluircurso, name='excluircurso'),

    #Alunos
    path('listaralunos', views.listaralunos, name='listaralunos'),

    path('alteraraluno/<int:codigo>', views.alteraraluno, name='alteraraluno'),

    path('incluiraluno', views.incluiraluno, name='incluiraluno'),

    path('excluiraluno/<int:codigo>', views.excluiraluno, name='excluiraluno'),

    #Professores
    path('listarprofessores', views.listarprofessores, name='listarprofessores'),

    path('alterarprofessor/<int:codigo>', views.alterarprofessor, name='alterarprofessor'),

    path('incluirprofessor', views.incluirprofessor, name='incluirprofessor'),

    path('excluirprofessor/<int:codigo>', views.excluirprofessor, name='excluirprofessor'),

    #Turmas
    path('listarturmas', views.listarturmas, name='listarturmas'),

    path('incluirturma', views.incluirturma, name='incluirturma'),
]