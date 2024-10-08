from django.forms import ModelForm
from cadastro.models import Curso

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'