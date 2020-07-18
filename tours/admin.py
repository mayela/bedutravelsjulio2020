from django.contrib import admin
from .models import User, Tour, Zona

class TourAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "slug", "operador", "tipoDeTour",
        "descripcion", "pais", "zonaSalida", "zonaLlegada")


admin.site.register(Tour, TourAdmin)
admin.site.register(User)
admin.site.register(Zona)

