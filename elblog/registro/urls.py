from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login" , views.login_request , name="Login"),
    path("signup" , views.signup , name="Signup"),
    path("logout" , LogoutView.as_view(template_name="Logout.html") , name="Logout"),
    path("userprofile" , views.userprofile , name="userprofile"),
    path("editprofile" , views.editprofile , name="editprofile"),
    path("viewprofile/<int:id>" , views.profile , name="viewprofile"),
    path("perfilautor/<int:id>" , views.perfilautor , name="perfilautor"),
]