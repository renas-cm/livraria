from django.contrib import admin

# Register your models here.

from backendLivraria.models.init import Categoria, Editora, Autor, Livro

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
