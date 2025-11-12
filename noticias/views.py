from django.shortcuts import render
from django.http import HttpResponse
from noticias.models import Categoria, Autor, Noticia

# Função
# Se def dentro classe = método
# Se def fora classe = função

def categorias(request):


    categorias = Categoria.objects.all()
    return render(request,
                  'noticias/index.html',
                  {'cards':categorias})

def autores(request):
    autores = Autor.objects.all()
    return render(request,'noticias/nossos_autores.html',{'autores':autores})

def index(request):
    noticias = Noticia.objects.all()
    return render(request,'noticias/index.html',{'noticias':noticias})


# return HttpResponse("<h1>Alô Django🚀</h1>")
    # Definindo um mock com dictionary
    """
       dados ={
         1:{"titulo":"mulheres dev",
            "conteudo":"mulheres programadores em python",
            "data_publicacao":"29/10/2025"},
         2:{"titulo":"programadores kids",
            "conteudo":"programadores em python no dia das crianças",
            "data_publicacao":"12/10/2025"},
          3: {"titulo": "Josias novo presidente",
              "conteudo": "Josias é nosso novo presidente, um homem de grande sonhos",
              "data_publicacao": "12/10/2025"},
      }
      """

"""
python manage.py shell
from noticias import Categoria
cat = Categoria(nome="")
cat.save()
Categoria.objects.all()
exit()
"""
