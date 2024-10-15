from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def serviços(request):
    return render(request, 'serviços.html')

def login(request):
    return render(request, 'login.html')