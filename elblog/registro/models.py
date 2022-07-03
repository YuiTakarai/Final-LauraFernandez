from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    imagen = models.ImageField(default='default.png' , null=True , blank=True , upload_to='avatares') 
    facebook = models.CharField(max_length=255 , null=True , blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__ (self):
        return str(self.user)