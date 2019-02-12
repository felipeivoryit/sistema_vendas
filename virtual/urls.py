from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.produto.view_home, name='view_produto_home'),
    url(r'^produto/(?P<pk>[0-9]+)$', views.produto.view_detalhes, name='view_produto_detalhes'),
    url(r'funcionario$', views.funcionario.ListaFuncionarios.as_view(), name='lista_funcionarios'),
    url('funcionario/cadastrar$', login_required(views.funcionario.FuncionarioCreateView.as_view()), name='cadastra_funcionario'),
    url(r'^funcionario/editar/(?P<pk>[0-9]+)$', views.funcionario.FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    url(r'^funcionario/remover/(?P<pk>[0-9]+)$', views.funcionario.FuncionarioDeleteView.as_view(), name='deletar_funcionario'),
    #url(r'^login$', login, {'template_name': 'usuario/login.html'}, name='login'),
    url(r'^login$', LoginView.as_view(template_name='usuario/login.html'), name="login"),
    url(r'^logout$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^login/cadastro$', login_required(views.usuario.register), name='cadastro_usuario'),
    url(r'^login/edicao$', login_required(views.usuario.edit), name='edicao_usuario'),
    url(r'^login/edicao/senha$', login_required(views.usuario.edit_password), name='edit_password'),
]
