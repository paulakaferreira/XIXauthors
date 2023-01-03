from django.db import models

class Auteur(models.Model):
    nom = models.CharField(null = False, blank = False, max_length = 200)
    prenom = models.CharField(null = False, blank = False, max_length = 100)

    def __str__(self) -> str:
        return self.nom.upper() + ', ' + self.prenom

class Livre(models.Model):
    titre = models.CharField(null = False, blank = False, max_length = 200)
    auteur = models.ManyToManyField(Auteur, blank = True)

