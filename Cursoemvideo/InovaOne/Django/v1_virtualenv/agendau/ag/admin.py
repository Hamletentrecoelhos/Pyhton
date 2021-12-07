from django.contrib import admin
from .models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    # Defina o que mais pode aparecer no display.(nesse caso, obejetos evento)
    list_filter = ('titulo', 'data_evento', 'data_criacao')
    # Filtro de seleção

admin.site.register(Evento, EventoAdmin)

