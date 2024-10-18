from django.shortcuts import render

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
    return render(request, 'sites.html')

def segurança(request):
    return render(request, 'segurança.html')