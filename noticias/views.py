from django.shortcuts import render
from django.http import HttpResponse
from noticias.models import Categoria
# Função
# Se def dentro classe = método
# Se def fora classe = função

def index(request):
    #return HttpResponse("<h1>Alô Django🚀</h1>")
    # Definindo um mock com dictionary

    """
    dados = {
        1:{"titulo":"Orientação de carreira para jovens",
           "conteudo":"Empresas trazem orientações de carreira para jovens",
           "data_publicacao":"29/10/2025"},

        2:{"titulo":"Resultado da Mega-Sena de hoje",
           "conteudo":"Resultados da Mega-Sena e números sorteados",
           "data_publicacao":"29/10/2025"},

        3:{"titulo":"Josias novo presidente",
           "conteudo":"Josias é o nosso novo presidente, um homem de sonhos.",
           "data_publicacao":"29/10/2025"},

    }
    """

    categorias = Categoria.objects.all()
    return render(request,
                  'noticias/index.html',
                  {'cards':categorias})
"""
python manage.py shell
from noticias import Categoria
cat = Categoria(nome="")
cat.save()
Categoria.objects.all()
exit()
"""