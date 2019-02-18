# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import CreateView
from django import forms
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
'''
# A user_passes_test receve um argumento obrigatório: um executável que recebe um objeto do
# tipo User e retorna True se é permitido ao usuário acessar a página.
'''
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import permission_required

from ..models import Produto

#def email_check(user):
    #return user.email.endswith('@lojavirtual.com.br')

# comando para verificar se o tem determinado e-mail
#@user_passes_test(email_check)
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

#@permission_required('virtual.produto.can_add_produto')
#@permission_required('auth.change_user', login_url="/login/")
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import user_passes_test


@method_decorator(permission_required('virtual.change_produto'), name='dispatch')
#@method_decorator(group_required('produto',))
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

def not_in_produto_group(user):
    if user:
        return user.groups.filter(name='produto').count() == 1
    return False

@login_required
@user_passes_test(not_in_produto_group, login_url='/login')
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
