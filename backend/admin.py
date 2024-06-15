from django.contrib import admin
from .models import Number  # Asegúrate de importar correctamente el modelo Number

class NumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'letter')
    search_fields = ('number', 'letter')

admin.site.register(Number, NumberAdmin)
