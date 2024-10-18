from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def dashboards(request):
    return render(request, 'dashboards.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def welcomeHomepage(request):
    return render(request, 'welcomeHomepage.html')

def sites(request):
    context = {}
    nestGuardSitesPage = NestGuardSitesPage.objects.all()
    nestGuardCard = NestGuardCard.objects.all()
    context['nestGuardSitesPage'] = nestGuardSitesPage
    context['nestGuardCard'] = nestGuardCard
    return render(request, 'sites.html', context)

def segurança(request):
    return render(request, 'segurança.html')