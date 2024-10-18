from django.db import models

# Create your models here.
class NestGuardDashboradPage(models.Model):
    titulo1 = models.TextField(blank=True, null=True)
    titulo2 = models.TextField(blank=True, null=True)
    titulo3 = models.TextField(blank=True, null=True)
    titulo4 = models.TextField(blank=True, null=True)
    descricao1 = models.TextField(blank=True, null=True)
    descricao2 = models.TextField(blank=True, null=True)
    descricao3 = models.TextField(blank=True, null=True)
    descricao4 = models.TextField(blank=True, null=True)
    imagem1 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem4 = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.titulo1
    
class NestGuardSitesPage(models.Model):
    titulo1 = models.TextField(blank=True, null=True)
    titulo2 = models.TextField(blank=True, null=True)
    titulo3 = models.TextField(blank=True, null=True)
    titulo4 = models.TextField(blank=True, null=True)
    descricao1 = models.TextField(blank=True, null=True)
    descricao2 = models.TextField(blank=True, null=True)
    descricao3 = models.TextField(blank=True, null=True)
    descricao4 = models.TextField(blank=True, null=True)
    imagem1 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem4 = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.titulo1


class NestGuardSegurançaPage(models.Model):
    titulo1 = models.TextField(blank=True, null=True)
    titulo2 = models.TextField(blank=True, null=True)
    titulo3 = models.TextField(blank=True, null=True)
    titulo4 = models.TextField(blank=True, null=True)
    descricao1 = models.TextField(blank=True, null=True)
    descricao2 = models.TextField(blank=True, null=True)
    descricao3 = models.TextField(blank=True, null=True)
    descricao4 = models.TextField(blank=True, null=True)
    imagem1 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem4 = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.titulo1
    
class NestGuardContatoPage(models.Model):
    titulo1 = models.TextField(blank=True, null=True)
    titulo2 = models.TextField(blank=True, null=True)
    titulo3 = models.TextField(blank=True, null=True)
    titulo4 = models.TextField(blank=True, null=True)
    descricao1 = models.TextField(blank=True, null=True)
    descricao2 = models.TextField(blank=True, null=True)
    descricao3 = models.TextField(blank=True, null=True)
    descricao4 = models.TextField(blank=True, null=True)
    imagem1 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem4 = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.titulo1
    
class NestGuardSobrePage(models.Model):
    titulo1 = models.TextField(blank=True, null=True)
    titulo2 = models.TextField(blank=True, null=True)
    titulo3 = models.TextField(blank=True, null=True)
    titulo4 = models.TextField(blank=True, null=True)
    descricao1 = models.TextField(blank=True, null=True)
    descricao2 = models.TextField(blank=True, null=True)
    descricao3 = models.TextField(blank=True, null=True)
    descricao4 = models.TextField(blank=True, null=True)
    imagem1 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem4 = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.titulo1
    
class NestGuardCard(models.Model):
    titulo = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    link_img = models.URLField(blank=True, null=True)
    descricaoModal = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo