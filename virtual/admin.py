# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Cliente, Funcionario, Endereco, Produto, Venda

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf']
    # Campos para pesquisa na listagem admin
    search_fields = ['nome', 'cpf']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao']
    # Campos para pesquisa na listagem admin
    search_fields = ['id', 'nome']

class FuncionarioAdmin(admin.ModelAdmin):
    # list_display = ['id', 'nome']
    # search_fields = ['id', 'nome']
    list_display = ['nome', 'sobrenome', 'tempo_de_servico', 'remuneracao']
    list_filter = ['tempo_de_servico']
    search_fields = ['nome', 'sobrenome']
    ordering = ['nome']
    empty_value_display = 'Não informado'


# Register your models here.
# models Cliente, Endereco
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda)
