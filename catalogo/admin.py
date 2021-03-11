from django.contrib import admin
from catalogo.models import Categoria, Produto, Usuario, Compra

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Compra)
