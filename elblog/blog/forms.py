from django  import forms
from blog.models import *
import datetime

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class Entrada_Blog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [ 'titulo' , 'subtitulo' , 'contenido' , 'categoria' , 'imagenblog']
        
        
class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = [ 'nombre' , 'cuerpo' , 'email']