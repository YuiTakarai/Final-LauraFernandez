from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registro.models import Profile

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'first_name' , 'last_name', 'password1' , 'password2']
        help_text = {k:"" for k in fields}
        widgets ={ 
                'password1' :forms.PasswordInput(),
                'password2' :forms.PasswordInput()
        }


class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar")
    first_name = forms.CharField(label="Ingresar su Nombre")
    last_name = forms.CharField(label="Ingresar su Apellido")
    password1 = forms.CharField(label="Ingresear Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'first_name' , 'last_name' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imagen', 'facebook', 'bio']