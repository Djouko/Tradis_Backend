from django.contrib.auth.models import User
from django.db import models

class Hebergement(models.Model):
    nom = models.CharField(max_length=255)  #Nom de l'hebergement
    lieu = models.CharField(max_length=255) #Lieu de l'hebergement
    MY_CHOICES = [  #Types d'hebergement
        (1, 'hotel'),
        (2, 'auberge'),
        (3, 'Particulier'),
    ]
    nature = models.IntegerField(choices=MY_CHOICES)    #Nature de l'hebergement
    description = models.TextField(blank=True)  #Description de l'hebergement
    photo = models.ImageField(upload_to='public', blank=True, null=True)    #Photo de presentation de l'hebergement
    video = models.FileField(upload_to='videos/')   #Video de presentation de l'hebergement
    Tarification = models.DecimalField(max_digits=5, decimal_places=2, default=0.0) #Tarification de l'hebergement
    Disponibilite = models.BooleanField(default=True)   #Disponibilite du logement
    nombre_piece = models.IntegerField()    #Nombre de pieces du logement
    latitude = models.FloatField(null=True)  # Longitude pour la localisation du lieu du logement
    longitude = models.FloatField(null=True)  # Latitude pour la localisation du lieu du logement

    def __str__(self):
        return self.nom


#Commentaires laisses par les utilisateurs sur un hebergement
class CommentaireHebergement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #Auteur du commentaire
    content = models.TextField()    #Contenu du commentaire
    hebergement = models.ForeignKey('Hebergement', null=False, on_delete=models.CASCADE) #Hebergement sur lequel on commente
    created_at = models.DateField(auto_now_add=True)    #Date de creation du commentaire
    updated_at = models.DateField(auto_now=True)    #Date de modification du commentaire


#Hebergement favoris definis par un utilisateur
class FavorisHebergement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #auteur qui defini ses Hebergement favoris
    hebergement = models.ForeignKey('Hebergement', null=False, on_delete=models.CASCADE) #Hebergement favoris defini par l'auteur en question