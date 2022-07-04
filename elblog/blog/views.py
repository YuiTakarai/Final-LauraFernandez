from django.shortcuts import get_object_or_404, render
from blog.models import *
from registro.models import *
from django.http import HttpResponse
import datetime
from django.template import loader
from blog.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    avatares = Profile.objects.filter(user=request.user.id)
    return render (request, "home.html", {'avatares': avatares})

def about(request):
    avatares = Profile.objects.filter(user=request.user.id)
    return render (request, "about.html", {'avatares': avatares})

@login_required
def menu(request):
    avatares = Profile.objects.filter(user=request.user.id)
    return render (request, "menu.html", {'avatares': avatares})

    
@login_required
def categorias(request):
    form = Categoria()
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "menu.html")
        else:
            return HttpResponse("Algo salió mal")
    return render (request, "categorias.html", {'form': form})


def listarcategorias(request):
    listado=Categoria.objects.all()
    return render(request, "listarcategorias.html", {'listado':listado})


def CategoryView(request, categoria_id):
    category_posts =Blog.objects.filter(categoria=categoria_id)
    avatares = Profile.objects.filter(user=request.user.id)
    return render (request, "category.html", {'categoria_id':categoria_id , 'category_posts': category_posts, 'avatares': avatares})

    
@login_required
def entrada_blog(request):
    form = Entrada_Blog()
    if request.method == "POST":
        form = Entrada_Blog(request.POST, request.FILES)
        if form.is_valid():
            #autor = form.cleaned_data['autor']
            titulo = form.cleaned_data['titulo']
            subtitulo = form.cleaned_data['subtitulo']
            contenido = form.cleaned_data['contenido']
            imagenblog = form.cleaned_data['imagenblog']
            categoria = form.cleaned_data['categoria']

            entradablog = Blog(autor=request.user , titulo=titulo , subtitulo=subtitulo, contenido=contenido , imagenblog=imagenblog , categoria=categoria ,publicado=datetime )
            entradablog.save()
            
            entrada = Blog.objects.all()
            return render (request, "blog.html" , {'entrada': entrada})  

    
    return render (request, "entrada_blog.html" , {'form': form})


def blog(request):
    entrada = Blog.objects.all()
    p = Paginator(entrada, 2)
    page = request.GET.get('page')
    entrada = p.get_page(page)
    avatares = Profile.objects.filter(user=request.user.id)
    return render (request , "blog.html" , {'entrada': entrada, 'avatares': avatares})

def detalle_blog(request, id):
    detalle = get_object_or_404(Blog , id=id)
    avatares = Profile.objects.filter(user=request.user.id)
    return render (request, "detalle_blog.html", {'detalle': detalle, 'avatares': avatares})
    
def agregar_comentario(request, id):
    detalle = Blog.objects.get(id=id)
    form = ComentarioForm(instance=detalle)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=detalle)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            cuerpo = form.cleaned_data['cuerpo']
            email = form.cleaned_data['email']

            comentarioingresado = Comentario(entrada=detalle , nombre=nombre , cuerpo=cuerpo , email=email , fecha=datetime )
            comentarioingresado.save()

            entrada = Blog.objects.all()
            return render (request, "blog.html" , {'entrada': entrada})  
    else:
        form = ComentarioForm()

    return render (request, "agregar_comentario.html" , {'form': form})

@login_required
def editar_entrada(request, id):
    entrada = Blog.objects.get(id = id)
    if entrada.autor == request.user.id:
        if request.method == "POST":
            form = Entrada_Blog(request.POST, request.FILES)
            if form.is_valid():
                datos = form.cleaned_data
                #entrada.autor = datos['autor']
                entrada.titulo = datos['titulo']
                entrada.subtitulo = datos['subtitulo']
                entrada.contenido = datos['contenido']
                entrada.imagenblog = datos['imagenblog']
                #entrada.publicado = datos['publicado']
                entrada.save()

                entrada = Blog.objects.all()
                return render (request, "blog.html" , {'entrada': entrada})
        else:
            form = Entrada_Blog(initial={'titulo': entrada.titulo , 'subtitulo': entrada.subtitulo , 'contenido': entrada.contenido , 'imagenblog': entrada.imagenblog ,'publicado': datetime})
        return render( request, "editar_entrada.html" , {'form': form , 'entrada': entrada} )
    return HttpResponse("El usuario no puede editar esta entrada")

@login_required
def eliminar_entrada(request, id):
    entrada = Blog.objects.get(id=id)
    if entrada.autor == request.user.id:
        entrada.delete()

        entrada = Blog.objects.all()

        return render (request, "blog.html" , {"entradas": entrada})
    else:
        return HttpResponse("El usuario no puede eliminar esta entrada")
