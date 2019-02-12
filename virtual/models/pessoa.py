from __future__ import unicode_literals

from django.db import models

class Pessoa(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(
            'Nome',
            max_length=50
        )
    sobrenome = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    data_nascimento = models.DateField(
            'Data de nascimento',
            null=True,
            blank=True
        )
    # metodo
    def __str__ (self):
        return self.nome

class Cliente(Pessoa):
    cpf = models.CharField(
        max_length=14,
        null=True,
        blank=True
    )
    compra_sempre = models.BooleanField(default=False)

class Endereco(models.Model):
    # chave estrangeira
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.CharField(
            'Endereço',
            max_length=100
        )
    # metodo
    def __str__ (self):
        return self.endereco

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

class Funcionario(Pessoa):
    tempo_de_servico = models.IntegerField(
        default=0
    )
    remuneracao = models.DecimalField(
        'Remuneração',
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    # metodo
    def __str__ (self):
        return self.nome

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
