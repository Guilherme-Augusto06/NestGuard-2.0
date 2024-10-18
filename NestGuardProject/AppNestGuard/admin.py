from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(NestGuardDashboradPage)
admin.site.register(NestGuardSitesPage)
admin.site.register(NestGuardSegurançaPage)
admin.site.register(NestGuardContatoPage)
admin.site.register(NestGuardCard)