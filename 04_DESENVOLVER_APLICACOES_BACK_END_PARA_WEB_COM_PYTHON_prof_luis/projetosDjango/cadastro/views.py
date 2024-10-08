from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Curso, Aluno, Professor
from cadastro.forms import AlunoForm, CursoForm, ProfessorForm

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

def incluircurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcursos')

    form = CursoForm()
    return render(request, 'form_curso.html', {'formulario':form})

def alterarcurso(request, codigo):
    c = Curso.objects.get(id=codigo)

    form = CursoForm(instance=c)
    return render(request, 'form_curso.html', {'formulario': form})

#Alunos
def listaralunos(request):
    alunos = Aluno.objects.order_by('nome')
    return render(request, 'listaralunos.html', {'alunos': alunos})

def incluiraluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaralunos')

    form = AlunoForm()
    return render(request, 'form_aluno.html', {'formulario':form})

def alteraraluno(request, codigo):
    a = Aluno.objects.get(id=codigo)

    form = AlunoForm(instance=a)
    return render(request, 'form_aluno.html', {'formulario': form})

#Professores
def listarprofessores(request):
    professores = Professor.objects.order_by('nome')
    return render(request, 'listarprofessores.html', {'professores': professores})

def incluirprofessor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarprofessores')

    form = ProfessorForm()
    return render(request, 'form_professor.html', {'formulario':form})

def alterarprofessor(request, codigo):
    p = Professor.objects.get(id=codigo)

    form = ProfessorForm(instance=p)
    return render(request, 'form_professor.html', {'formulario': form})