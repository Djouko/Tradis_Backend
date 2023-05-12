from django.db import models
from django.contrib.auth.models import User

#SItes touristiques
class Sites(models.Model):
    title = models.CharField(max_length=255)    #Nom du site
    lieu = models.CharField(max_length=255)   #ou encore pays du site
    description = models.TextField(blank=True)      #description du site
    attachement = models.FileField(upload_to='public', null=True)   #Photo de presentation du site
    video = models.FileField(upload_to='videos/', null=True)    #Video de presentation du site touristique
    latitude = models.FloatField(default=0.0, null=True)  #Longitude pour la localisation d'un site touristique
    longitude = models.FloatField(default=0.0, null=True) #Latitude pour la localisation d'un site touristique
    informations = models.TextField(blank=True) #Information sur les agences de voyage qui mènent à cette destination
    local_guide_available = models.BooleanField(default=False)    #Mentionne s'il y a au moins un local guide pour ce site touristique
    prix = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)     #Dire si le site touristique est payant ou pas
    createdAt = models.DateField(auto_now_add=True)     #Date de creation d'un site touristique
    updatedAt = models.DateField(auto_now=True)     #Date de modification d'un site touristique

    categorie = models.ForeignKey('Categories', null=False, on_delete=models.CASCADE)    #Categorie du site touristique

    def __str__(self):
        return  self.title

#Categorie des sites touristiques
class Categories(models.Model):
    name = models.CharField(max_length=255)     #Nom de la categorie d'un site touristique

    class Meta:
        verbose_name = 'Site touristique'
        verbose_name_plural = 'Sites touristiques'

    def __str__(self):
        return self.name

#Commentaires laisses par les utilisateurs sur les sites touristiques
class CommentaireSite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #Auteur du commentaire
    content = models.TextField()    #Contenu du commentaire
    site = models.ForeignKey('Sites', null=False, on_delete=models.CASCADE) #Site touristique sur lequel on commente
    created_at = models.DateField(auto_now_add=True)    #Date de creation du commentaire
    updated_at = models.DateField(auto_now=True)    #Date de modification du commentaire

#Sites favoris definis par un utilisateur
class FavorisSite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #auteur qui defini ses sites favoris
    site = models.ForeignKey('Sites', null=False, on_delete=models.CASCADE) #site favoris defini par l'auteur en question


class LocalGuide(models.Model):
    nom_guide = models.CharField(max_length=255, null=True)  # Nom du local guide
    prenom_guide = models.CharField(max_length=255, null=True)  # Prenom du local guide
    presentation_guide = models.TextField(blank=True)  # présentation incluant la manière dont il compte prendre les touriste depuis l’agence de voyage
    profile_guide = models.FileField(upload_to='public', null=True)  # Photo de profil du local guide
    numero_telephone = models.CharField(max_length=20, null=True)  # Numero de telephone du local guide
    cni_guide = models.FileField(upload_to='public', null=True)  # Cni du local guide
    site = models.ForeignKey(Sites, on_delete=models.CASCADE, related_name='local_guides')  #Site touristique sur lequel le local guide desire travailler
    available = models.BooleanField(default=False)  #Marque s'il est disponible ou pas