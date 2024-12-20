from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def dashboards(request):
    context = {}
    nestGuardDashboradPage = NestGuardDashboradPage.objects.all()
    context['nestGuardDashboradPage'] = nestGuardDashboradPage
    return render(request, 'dashboards.html', context)


