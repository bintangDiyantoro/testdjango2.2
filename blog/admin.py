from django.contrib import admin
<<<<<<< HEAD
from .models import Artikel
=======
from .models import *
>>>>>>> Bean


class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Artikel,ArtikelAdmin)