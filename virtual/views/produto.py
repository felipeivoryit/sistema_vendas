# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
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
