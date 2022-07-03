from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required 
from django.template import loader
from registro.models import *
from blog.models import *
from registro.forms import *
from django.http import HttpResponse

# Create your views here.

def signup(request):

    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Login')
        else:
            return HttpResponse("Algo salió mal")
    else:
        form = UserCreateForm()
    return render( request , "signup.html" , {"form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data= request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=clave)

            if user is not None:
                login(request,user)
                return redirect('home')


            else:
                return HttpResponse("Algo salió mal")
        else:         
            return HttpResponse(f"Ooops, algo salió mal {form}")

    form = AuthenticationForm()

    return render( request , "login.html" , {"form":form})


@login_required
def editprofile(request):

    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            usuario.email = datos['email']
            usuario.first_name = datos['first_name']
            usuario.last_name = datos['last_name']
            password = datos['password1']
            usuario.set_password(password)
            usuario.save()

            return render( request , "home.html")
    else:
        form = UserEditForm(initial={'email':usuario.email , 'first_name': usuario.first_name , 'last_name': usuario.last_name})
    return render( request , "editprofile.html" , {"form":form , "usuario":usuario})

@login_required
def userprofile(request):
    
    if request.method == "POST":
        form = ProfileForm(request.POST , request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponse ("Imagen Guardada")
    else:
        form = ProfileForm()

        return render(request, "userprofile.html" , {'form': form})


def profile(request, id):
    detalle = get_object_or_404(User, id=id)
    detalle2 = get_object_or_404(Profile, id=id)
    publicaciones = Blog.objects.filter(autor_id=request.user.id)
    avatares = Profile.objects.filter(user=request.user.id)
    return render(request, "profile.html" , {'detalle': detalle , 'detalle2': detalle2, 'publicaciones': publicaciones, 'avatares': avatares})



