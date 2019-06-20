from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from .models import *


def Login(request,template_name='login.html'):
    next=request.GET.get('next','dashboard/')
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            messages.error(request,'Usuário ou senha incorretos')
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request,template_name,{'redirect_to':next})

def deslogar(request):
   logout(request)
   return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def dashboard(request,template_name='dashboard.html'):

    return render(request,template_name,{})

@login_required
def resistrarUsuario(request, template_name='userNew.html'):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        tipo=request.POST['tipo-user']
        if tipo=='Administrador':
            user=User.objects.create_user(username,email,password)
            user.is_staff=True
            user.save()
        else:
            user=User.objects.create_user(username,email,password)
        return redirect('Colaborador/listuser/')
    return render(request,template_name,{})

@login_required
def ListarUsuario(request,template_name='listuser.html'):
    usuario=User.objects.all()

    usuarios={'usuario':usuario}
    return render(request,template_name,usuarios)

class ColaboraForm(ModelForm):
    class Meta:
        model=Colaborador
        fields=['nome','nascimento','rg','cpf','sexo_choices']

@login_required
def ColaboradorNew(request, template_name='colaboradorNew.html'):
    form=ColaboraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Colaborador/dashboard/')
    return render(request,template_name,{'form':form})

@login_required
def ListarColaborador(request,template_name='listarcolaborador.html'):
    colaborador=Colaborador.objects.all()

    colaboradores={'colaborador':colaborador}

    return render(request,template_name,colaboradores)

class FormacaoForm(ModelForm):
    class Meta:
        model=Formacao
        fields=['colaborador','tipo','nome_curso','dt_inicio','dt_termino']

@login_required
def FormacaoNew(request,template_name='formacaoNew.html'):
    form=FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Formação Cadastrada Com Sucesso!')
        return redirect('Colaborador/listarFormacao')
    colaborador=Colaborador.objects.all()
    return render(request, template_name,{'form':form})


@login_required
def ListarFormacao(request,template_name='listarFormacao.html'):
    formacao=Formacao.objects.all()
    formacoes={'formacao':formacao}
    return render(request,template_name,formacoes)
