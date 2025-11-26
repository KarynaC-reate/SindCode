from django.urls import path
from noticias.views import index
from noticias.views import autores
from noticias.views import buscar
from noticias.views import retornar
from noticias.views import todas_noticias
from noticias import views

urlpatterns = [
    path('',index),
    path('autor/',autores),
    path("buscar",buscar, name='buscar'),
    path("retornar",retornar, name='retornar'),
    path('noticia/<int:noticia_id>', views.detalhe_noticia, name='detalhe_noticia'),
    path("todas_noticias",todas_noticias, name='todas_noticias'),

]