from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Aluno

# Create your views here.
def index(request):
    return render(request, 'inicio.html')

def segundo(request):
    return HttpResponse("<h1>Segunda</h1>")

def pagina(request):
    return render(request, 'pagina.html')

def mensagem(request):
    return render(request, 'inicio.html')

#Cursos
def listarcursos(request):
    cursos = Curso.objects.order_by('nome')
    return render(request, 'listarcursos.html', {'cursos': cursos})

def listaralunos(request):
    alunos = Aluno.objects.order_by('nome')
    return render(request, 'listaralunos.html', {'alunos': alunos})