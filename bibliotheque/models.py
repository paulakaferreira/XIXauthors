from django.db import models


class Personne(models.Model):
    nom = models.CharField(null=False, blank=False, max_length=200)
    prenom = models.CharField(null=False, blank=False, max_length=100)
    date_naissance = models.DateField(null=True)
    date_mort = models.DateField(null = True)
    lieu_naissance = models.CharField(null=False, blank=False, max_length=200)
    conjoint = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

class Auteur(Personne):
    def __str__(self) -> str:
        return self.nom.upper() + ", " + self.prenom.title()

class Livre(models.Model):
    titre = models.CharField(null=False, blank=False, max_length=200)
    auteur = models.ManyToManyField(Auteur, blank=True)