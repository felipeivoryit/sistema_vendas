from __future__ import unicode_literals

from django.db import models
from .pessoa import Cliente

class Produto(models.Model):
    nome = models.CharField(
        max_length=100
    )
    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    descricao = models.CharField(
        'descrição',
        max_length=200,
        null=True,
        blank=True
    )

    def __str__(self):
        return '{}'.format(self.pk)
        # estudar quando preciso passar mais dados

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    data_venda = models.DateTimeField(auto_now_add=True)
