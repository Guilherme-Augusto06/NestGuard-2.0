from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),    
    path('serviços', views.serviços, name="serviços"),   
    path('login', views.login, name="login"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('homepage', views.welcomeHomepage, name="welcomeHomepage"),
]