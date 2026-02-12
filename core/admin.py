from django.contrib import admin

from .models import Protudo
class ProdutoAdm(admin.ModelAdmin):
    list_display = ('nome','preco','qtde','data_de_validade')

admin.site.register(Protudo,ProdutoAdm)
