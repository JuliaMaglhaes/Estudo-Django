from django.contrib import admin
from disco.models import Bandas, Albuns, Musicas

class AlbunsAdmin(admin.ModelAdmin):
    list_display =[
        'titulo',
        'banda',
        'data',
    ]

class MusicasAdmin(admin.ModelAdmin):
    list_display =[
        'titulo',
        'segundos',
        'album',
    ]

admin.site.register(Albuns, AlbunsAdmin)
admin.site.register(Bandas)
admin.site.register(Musicas, MusicasAdmin)