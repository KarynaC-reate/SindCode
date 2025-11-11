from django.shortcuts import render
from django.http import HttpResponse
from noticias.models import Categoria, Autor

# Função
# Se def dentro classe = método
# Se def fora classe = função

def index(request):
    #return HttpResponse("<h1>Alô Django🚀</h1>")
    # Definindo um mock com dictionary

    categorias = Categoria.objects.all()
    return render(request,
                  'noticias/index.html',
                  {'cards':categorias})

def autores(request):
    autores = Autor.objects.all()
    return render(request,'noticias/nossos_autores.html',{'autores':autores})

"""
python manage.py shell
from noticias import Categoria
cat = Categoria(nome="")
cat.save()
Categoria.objects.all()
exit()
"""
