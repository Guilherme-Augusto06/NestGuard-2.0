from django.db import models


    
class NestGuardCard(models.Model):
    titulo = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    link_img = models.URLField(blank=True, null=True)
    descricaoModal = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    


class Orcamento(models.Model):
    nome_cliente = models.CharField(max_length=100, verbose_name="Nome do Cliente")
    telefone_cliente = models.CharField(max_length=15, verbose_name="Telefone do Cliente")
    email_cliente = models.EmailField(verbose_name="Email do Cliente")
    descricao_servico = models.TextField(verbose_name="Descrição do Serviço")
    data_entrega = models.DateField(verbose_name="Data de Entrega")
    tipo_servico = models.CharField(
        max_length=50,
        choices=[
            ('criar_site', 'Criação de site'),
            ('criar_design', 'Criação de design'),
            ('criar_bot', 'Criação de bot'),
            ('hospedagem', 'Hospedagem'),
            ('automacao', 'Automação'),

            ('outros', 'Outros')
        ],
        verbose_name="Tipo de Serviço"
    )
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"{self.nome_cliente} - {self.tipo_servico}"
