from django.contrib import admin
from . import models


@admin.register(models.Auteur)
class AuteurAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "titre",
    ]
    search_fields = ["titre", "auteur__nom", "auteur__prenom"]
