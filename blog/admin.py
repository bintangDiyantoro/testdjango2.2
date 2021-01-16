from django.contrib import admin
from .models import Artikel


class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Artikel,ArtikelAdmin)