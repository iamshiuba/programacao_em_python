from django import forms
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
    dataInicio = forms.DateTimeField(
        label='Data de Início',
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M:%S',
            attrs={ 'type': 'datetime-local'}
        ),
        input_formats=('%Y-%m-%d %H:%M:%S'),
    )
    dataTermino = forms.DateTimeField(
        label='Data de Término',
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M:%S',
            attrs={ 'type': 'datetime-local'}
        ),
        input_formats=('%Y-%m-%d %H:%M:%S'),
    )