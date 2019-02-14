# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import CreateView
from django import forms
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse

from ..models import Produto

def view_home(request):
    #return HttpResponse("Exemplo.")
    # retornar todos os produtos cadastrados no sistema
    produtos = Produto.objects.all()
    # adicionando objeto contendo os produtos cadastrados
    contexto ={
        'produtos': produtos,
        #'titulo': 'Produtos cadastrados'
    }

    return render(
        request,
        'produto/home.html',
        contexto
    )

class InsereProdutoForm(forms.ModelForm):
    class Meta:
        # modelo base
        model = Produto

        # campos que estarao no from
        fields = [
            'nome',
            'valor',
            'descricao',
            'image',
            'document'
        ]

class ProdutoCreateView(SuccessMessageMixin, CreateView):
    template_name = "produto/cadastro_edicao.html"
    form_class = InsereProdutoForm
    success_message = 'Produto cadastrado com sucesso!'

    # Função fornece os dados do contecto a ser usado ao rederizar um template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variavel_titulo'] = 'Cadastrar produto'
        return context

    success_url = reverse_lazy("cadastro_produto")

def view_detalhes(request, pk):
    # tratar quando o código não é válido, gera uma exceção
    try:
        #produto = Produto.objects.get(pk=pk)
        # busca o produto apartir do id (pk)
        produto = Produto.objects.filter(pk=pk).first()
    except Produto.DoesNotExist:
        produto = None

    contexto ={
        'produto': produto
    }

    return render(
        request,
        'produto/detalhes.html',
        contexto
    )
