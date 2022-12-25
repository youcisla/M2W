from django.urls import path
from M2W import views
from .models import SignUpView
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="home"),
    # path('ctrl=chihaja+signout/', views.signout),
]