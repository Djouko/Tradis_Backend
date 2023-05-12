from django.test import TestCase

# Create your tests here.
from sites.models import Sites, Categories


class SitesTestCase(TestCase):
    DUMMY_SITES_TITLE = "Phalaises du nkam"

    def setUp(self):
        self.sitesTouristiques = Categories()
        self.sitesTouristiques.name = "Phalaises"
        self.sitesTouristiques.save()

        self.sitesTouristiquesTestElement = Sites()
        self.sitesTouristiquesTestElement.title = self.DUMMY_SITES_TITLE
        self.sitesTouristiquesTestElement.list = self.sitesTouristiques
        self.sitesTouristiquesTestElement.save()

    def test_create_sites(self):
        nbr_of_stes_before_add = Sites.objects.count()
        new_site = Sites()
        new_site.title = "Phalaises de Dschang"
        new_site.list = self.sitesTouristiques
        new_site.save()
        nbr_of_sites_after_add = Sites.objects.count()
        self.asserTrue(nbr_of_sites_after_add == nbr_of_stes_before_add + 1)
        #voir combien sont present dans notre DB
        #Ajouter un objet dans notre DB
        #Valider que le nombre d'objets de la base de donnees a ete incremente de 1

    def test_update_sites(self):
        self.assertEqual(self.sitesTouristiquesTestElement.title, self.DUMMY_SITES_TITLE)
        self.sitesTouristiquesTestElement.title = "Changed"
        self.sitesTouristiquesTestElement.save()

        tempElement = Sites.objects.get(pk=self.sitesTouristiquesTestElement.pk)
        self.assertEqual(tempElement, "Changed")