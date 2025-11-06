from django.contrib import admin

import noticias.models as nt


admin.site.register(nt.Categoria)
admin.site.register(nt.Autor)
