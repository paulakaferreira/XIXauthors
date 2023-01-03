from django.contrib import admin
from . import models


@admin.register(models.Auteur)
class AuteurAdmin(admin.ModelAdmin): ...

@admin.register(models.Livre)
class LivreAdmin(admin.ModelAdmin): ...
