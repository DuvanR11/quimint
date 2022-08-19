from django.contrib import admin
from .models import *
# Register your models here.
class categoriasAdmin(admin.ModelAdmin):
    pass
class equiposAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categorias, categoriasAdmin)
admin.site.register(Equipos, equiposAdmin)