from django.db import models


class Personne(models.Model):

    GENRE_CHOICES = [
        ("F", "Féminin"),
        ("M", "Masculin")
    ]

    nom = models.CharField(null=False, blank=False, max_length=200)
    prenom = models.CharField(null=False, blank=False, max_length=100)
    genre = models.CharField(choices=GENRE_CHOICES,
        null=True, blank=True, max_length=1)


class Auteur(Personne):
    date_naissance = models.DateField(null=True)
    date_mort = models.DateField(null=True)
    lieu_naissance = models.CharField(null=False, blank=False, max_length=200)
    conjoint = models.ForeignKey(
        Personne, related_name="conjoint_rn", null=True, blank=True, on_delete=models.SET_NULL
    )
    mere = models.ForeignKey(
        Personne, related_name="enfant_mere", null=True, blank=True, on_delete=models.SET_NULL
    )
    pere = models.ForeignKey(
        Personne, related_name="enfant_pere", null=True, blank=True, on_delete=models.SET_NULL
    )
    def __str__(self) -> str:
        return self.nom.upper() + ", " + self.prenom.title()


class FaitHistorique(models.Model):
    description = models.TextField(null=False, blank=False)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    auteur = models.ManyToManyField(Auteur, blank=True)

    class Meta:
        verbose_name_plural = "Faits Historiques"


class Courant(models.Model):
    titre = models.CharField(null=False, blank=False, max_length=200)
    caracteristiques = models.TextField(null=True, blank=True)


class Livre(models.Model):
    titre = models.CharField(null=False, blank=False, max_length=200)
    auteur = models.ManyToManyField(Auteur, blank=True)
    courant = models.ManyToManyField(Courant, blank=True)
