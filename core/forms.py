from django.forms import ModelForm
from .models import Curso, Emprego, Cliente



class CursosForm(ModelForm):
    class Meta:
           model = Curso
           fields = ['titulo', 'vagas']


class EmpregoForm(ModelForm):
    class Meta:
           model = Emprego
           fields = ['titulo', 'vagas','empresa', 'foto']

class ClienteForm(ModelForm):
    class Meta:
           model = Cliente
           fields = ['nome', 'telefone','email', 'endereco', 'foto']
