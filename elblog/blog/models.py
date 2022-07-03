from django.db import models
import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Blog(models.Model):
    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    contenido = RichTextField()
    publicado = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria ,related_name="categoria" , on_delete=models.CASCADE)
    imagenblog = models.ImageField(default='03.jpg' , null=True , blank=True , upload_to='posteos')

    class Meta:
        ordering = ['-publicado']
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    entrada = models.ForeignKey(Blog, related_name="comentario" , on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    cuerpo = models.TextField()
    email = models.EmailField()
    fecha = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return self.nombre