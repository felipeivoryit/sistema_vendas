from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm

from ..forms import RegisterForm, EditUsuarioForm

def register(request):
    template_name = 'usuario/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def edit(request):
    template_name = 'usuario/edit.html'
    context = {}
    # verificando se o método é post para verificar o return
    if request.method == 'POST':
        # instance=request.user usuário atual da sessão
        form = EditUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditUsuarioForm(instance=request.user)
            context['success'] = True
    else:
        form = EditUsuarioForm(instance=request.user)
    context['form'] = form

    return render(request, template_name, context)

def edit_password(request):
    template_name = 'usuario/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
