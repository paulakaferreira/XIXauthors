from django.test import TestCase

from bibliotheque import models


class AuteurTestCase(TestCase):
    def setUp(self):
        models.Auteur.objects.create(nom="de assis", prenom="machado")
        models.Auteur.objects.create(nom="lispector", prenom="clarice")

    def test_string_representation_machado(self):
        "String representation complies to `NOM, Prenom` format."
        machado = models.Auteur.objects.get(nom="de assis", prenom="machado")
        self.assertEqual(str(machado), "DE ASSIS, Machado")

    def test_string_representation_clarice(self):
        "String representation complies to `NOM, Prenom` format."
        clarice = models.Auteur.objects.get(nom="lispector", prenom="clarice")
        self.assertEqual(str(clarice), "FALCAO, Clarice")
