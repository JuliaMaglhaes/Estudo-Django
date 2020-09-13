from django.forms import ModelForm
from .models import Musicas
from django.forms import TextInput

class MusicasForm(ModelForm):
    class Meta:
        model = Musicas
        fields = ['titulo','segundos', 'album']
        widgets = {
                    'titulo': TextInput(attrs={'autofocus':'autofocus'})
                }
