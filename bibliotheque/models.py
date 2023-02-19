from django.db import models


class Personne(models.Model):

    GENRE_CHOICES = [
        ("F", "Féminin"),
        ("M", "Masculin"),
        ("A", "Autre")
    ]

    nom = models.CharField(null=False, blank=False, max_length=200)
    prenom = models.CharField(null=False, blank=False, max_length=100)
    genre = models.CharField(choices=GENRE_CHOICES,
        null=True, blank=True, max_length=1)
    mere = models.ForeignKey(
        "self", related_name="enfants_mere", null=True, blank=True, on_delete=models.SET_NULL
    )
    pere = models.ForeignKey(
        "self", related_name="enfants_pere", null=True, blank=True, on_delete=models.SET_NULL
    )
    conjoint = models.OneToOneField(
        "self", related_name="conjoint_rn", null=True, blank=True, on_delete=models.SET_NULL
    )
    amis = models.ManyToManyField(
        "self", blank=True
    )
    secondaire = models.ManyToManyField(
        "self", blank=True
    )


class FaitMarquant(models.Model):
    description = models.TextField(null=False, blank=False)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Faits Marquants"

class Auteur(Personne):
    date_naissance = models.DateField(null=True)
    date_mort = models.DateField(null=True)
    lieu_naissance = models.CharField(null=False, blank=False, max_length=200)
    faitmarquant = models.ManyToManyField(FaitMarquant, blank=True)
  
    def __str__(self) -> str:
        return self.nom.upper() + ", " + self.prenom.title()

class FaitSocial(models.Model):
    description = models.TextField(null=False, blank=False)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    auteur = models.ManyToManyField(Auteur, blank=True)

    class Meta:
        verbose_name_plural = "Faits Sociaux"


class Courant(models.Model):
    nom = models.CharField(null=False, blank=False, max_length=200)
    caracteristiques = models.TextField(null=True, blank=True)

class Genre(models.Model):
    nom = models.CharField(null=False, blank=False, max_length=200)
    caracteristiques = models.TextField(null=True, blank=True)


class Livre(models.Model):
    titre = models.CharField(null=False, blank=False, max_length=200)
    auteur = models.ManyToManyField(Auteur, blank=True)
    courant = models.ManyToManyField(Courant, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)

class Edition(models.Model):
    livre = models.ForeignKey(Livre, null=True, blank=True, on_delete=models.SET_NULL)
    annee = models.DateField(null=True)
    langue = models.CharField(null=False, blank=False, max_length=200)
    ville = models.CharField(null=False, blank=False, max_length=200)
    pays = models.CharField(null=False, blank=False, max_length=200)
    editeur = models.CharField(null=False, blank=False, max_length=200)
    imprimerie = models.CharField(null=False, blank=False, max_length=200)
