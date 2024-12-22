from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')




def orcamento(request):
    return render(request, 'orcamento.html')

def registro_orcamento(request):
    return render(request, 'registro_orcamento.html')