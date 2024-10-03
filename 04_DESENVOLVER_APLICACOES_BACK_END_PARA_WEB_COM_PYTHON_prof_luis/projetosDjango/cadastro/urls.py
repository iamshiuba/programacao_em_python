from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segundo', views.segundo, name='segundo'),

    path('pagina', views.pagina, name='pagina'),

    path('mensagem', views.mensagem, name='mensagem'),

    #Curso
    path('listarcursos', views.listarcursos, name='listarcursos'),
    path('listaralunos', views.listaralunos, name='listaralunos'),
]