from django.shortcuts import render, redirect
from associados.forms import AssociadoForm, LoginForms
from django.contrib.auth.models import User
from django.contrib import auth


def associados(request):
    return render(request, 'associados/index.html')


def login(request):
    form = LoginForms()
    form = LoginForms(request.POST)

    # Verificar envio da requisição
    if request.method == 'POST':
        # Se a requisição for POST (tentativa de login)
        nome = form['nome_login'].value()
        senha = form['senha'].value()
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if usuario is not None:
            # Se o usuário for autenticado com sucesso
            auth.login(request, usuario)
            return redirect('beneficios')

        # Se o login falhar (usuario é None), o fluxo continua para a linha
        # que renderiza o formulário com a variável 'form' (que pode ter erros).

    # Se a requisição não for POST (é GET, ou POST falhou)
    return render(request, 'associados/login.html', {'form': form})

def cadastro(request):
    form = AssociadoForm()
    if request.method == 'POST':
            return redirect('login')


    return render(request, 'associados/cadastro.html',{'form': form})
