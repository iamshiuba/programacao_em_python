from django.forms import ModelForm
from cadastro.models import Curso, Aluno, Professor, Turma

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'