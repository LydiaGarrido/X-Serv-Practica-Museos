from django.contrib import admin
from museos.models import Museo, Comentarios, Configuracion
from museos.models import Seleccion
# Register your models here.

admin.site.register(Museo)
admin.site.register(Comentarios)
admin.site.register(Configuracion)
admin.site.register(Seleccion)
