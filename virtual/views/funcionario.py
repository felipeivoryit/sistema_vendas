from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone
from django.core.paginator import Paginator

# biblioteca para verificar se está autenticado
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


from ..models import Funcionario

def not_in_funcionario_group(user):
    if user:
        return user.groups.filter(name='funcionario').count() == 1
    return False

@method_decorator(user_passes_test(not_in_funcionario_group), name='dispatch')
class ListaFuncionarios(ListView):
    template_name = "funcionario/lista_funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(ListaFuncionarios, self).get_context_data(**kwargs)

        # criando parametros que serão adicionado a paginação caso necessário
        parametros = ''
        for item, value in self.request.GET.dict().items():
            if not item == 'page':
                parametros += '&{}={}'.format(item, value)
                context[item] = value

        parametros = parametros.replace(' ', '+')

        context['parametros'] = parametros

        return context

    def get_queryset(self):
        queryset = Funcionario.objects.all()
        if self.request.GET.get("tempo_de_servico"):
            selection_tempo_servico = self.request.GET.get("tempo_de_servico")
            if ( selection_tempo_servico != 'todos'):
                queryset = Funcionario.objects.filter(tempo_de_servico=selection_tempo_servico)
        if self.request.GET.get("busca"):
            busca = self.request.GET.get("busca")
            queryset = Funcionario.objects.filter(nome__icontains=busca)

        return queryset

    '''
    def get_context_data(self, **kwargs):
        page = self.request.GET.get('page')
        print(page)
    '''


class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        # modelo base
        model = Funcionario

        # campos que estarao no from
        fields = [
            'nome',
            'sobrenome',
            'remuneracao'
        ]

#@login_required
@method_decorator(user_passes_test(not_in_funcionario_group), name='dispatch')
class FuncionarioCreateView(SuccessMessageMixin, CreateView):

    template_name = "funcionario/cadastro_edicao.html"
    form_class = InsereFuncionarioForm
    success_message = 'Funcionário cadastrado com sucesso!'

    # Função fornece os dados do contecto a ser usado ao rederizar um template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variavel_titulo'] = 'Cadastrar funcionário'
        return context

    success_url = reverse_lazy("cadastro_funcionario")

    #def form_invalid(self, form):
    #     return self.render_to_response(self.get_context_data(form=form))

class FuncionarioUpdateView(SuccessMessageMixin, UpdateView):

    template_name = "funcionario/cadastro_edicao.html"
    model = Funcionario
    form_class = InsereFuncionarioForm

    #objetoFuncionario = Funcionario.objects.all()

    # Retornando o objeto
    context_object_name = "Funcionario"
    # Retorna mensagem de sucesso quando editado
    #success_message = 'Funcionário editado com sucesso!'

    # Construtor
    def __init__(self):
        self.erro = False
        self.sucesso = False

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        self.sucesso = True
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        self.erro = True
        return self.render_to_response(self.get_context_data(form=form))


    # Função fornece os dados do contecto a ser usado ao rederizar um template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variavel_titulo'] = 'Editar funcionário'
        if self.erro:
            context['variavel_error'] = self.erro

        if self.sucesso:
            context['variavel_sucesso'] = self.sucesso
            context['variavel_sucesso_tipo'] = "edicao"

        return context

    #success_url = reverse_lazy("lista_funcionarios")
    # Use a estrutura de mensagens do Django para esse propósito, altere get_success_url com a mensagem.
    '''
    def get_success_url(self, **kwargs):
        return reverse('atualiza_funcionario', kwargs={
            'pk': self.object.pk
        },)
    '''

class FuncionarioDeleteView(SuccessMessageMixin, DeleteView):

    model = Funcionario

    success_url = reverse_lazy("lista_funcionarios")
