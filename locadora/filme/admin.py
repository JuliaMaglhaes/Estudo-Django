from django.contrib import admin
from .models import Filme
from .models import Generos

admin.site.register(Filme)
admin.site.register(Generos)
