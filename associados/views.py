from django.shortcuts import render, redirect
from associados.forms import AssociadoForm

def associados(request):
    return render(request, 'associados/index.html')

def login(request):
    return render(request, 'associados/login.html')

def cadastro(request):
    form = AssociadoForm()
    if request.method == 'POST':
        form = AssociadoForm(request.POST)
        if form['senha1'].value() != form['senha2'].value():
            return redirect(cadastro)
    return render(request, 'associados/cadastro.html',{'form': form})