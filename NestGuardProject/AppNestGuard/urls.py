from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.homepage, name="homepage"),    
    path('orcamento', views.orcamento, name="orcamento"),
    path('registro-orcamento/', registro_orcamento, name='registro_orcamento'),

]