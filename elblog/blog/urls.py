from django.urls import path
from blog import views
from .views import CategoryView

urlpatterns = [
    path('' , views.blog, name="home"),
    path('about' , views.about , name="about"),
    path('menu' , views.menu , name ="menu"),
    path('categorias' , views.categorias, name="categorias"),
    path('listarcategorias', views.listarcategorias, name="listarcategorias"),
    path('entrada_blog' , views.entrada_blog , name = "entrada_blog"),
    path('blog' , views.blog , name = 'blog'),
    path('detalle_blog/<int:id>' , views.detalle_blog , name="detalle_blog"),
    path('detalle_blog/<int:id>/agregar_comentario' , views.agregar_comentario , name="agregar_comentario"),
    path('editar_entrada/<int:id>' , views.editar_entrada , name="editar_entrada"),
    path('eliminar_entrada/<int:id>' , views.eliminar_entrada , name="eliminar_entrada"),
    path('category/<int:categoria_id>', CategoryView, name="category"),

]   