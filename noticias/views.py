from django.shortcuts import render
from django.http import HttpResponse

# Função
# Se def dentro classe = metodo
# Se def fora classe = funcao

def index(request):
    #return HttpResponse("<h1>Alô Django🚀</h1>")
    return render(request, 'noticias/index.html')
