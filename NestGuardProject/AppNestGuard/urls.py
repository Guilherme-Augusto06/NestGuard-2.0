from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),    
    path('dashboards', views.dashboards, name="dashboards"),   
    path('login', views.login, name="login"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('homepage', views.welcomeHomepage, name="welcomeHomepage"),
    path('sites', views.sites, name="sites"),
    path('segurança', views.segurança, name="segurança"),
]