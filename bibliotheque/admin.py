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


@admin.register(models.Personne)
class PersonneAdmin(admin.ModelAdmin):
    ...


@admin.register(models.FaitSocial)
class FaitSocialAdmin(admin.ModelAdmin):
    ...



@admin.register(models.FaitMarquant)
class FaitMarquantAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Courant)
class CourantAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    ...
