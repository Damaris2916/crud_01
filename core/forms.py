from django.forms import ModelForm
from .models import Curso


class CursosForm(ModelForm):
    class Meta:
           model = Curso
           fields = ['titulo', 'vagas']
