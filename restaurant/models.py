from django.contrib.auth.models import User
from django.db import models

class Restaurant(models.Model):
    nom = models.CharField(max_length=255)  #Nom du restaurant
    lieu = models.CharField(max_length=255) #Lieu du restaurant
    description = models.TextField(blank=True)  #Description du restaurant
    photo = models.ImageField(upload_to='public', blank=True, null=True)    #Photo de presentation du menu du restaurant
    latitude = models.FloatField(null=True)  # Longitude pour la localisation du lieu du restaurant
    longitude = models.FloatField(null=True)  # Latitude pour la localisation du lieu du restaurant

    def __str__(self):
        return self.nom


#Commentaires laisses par les utilisateurs sur un restaurant
class CommentaireRestaurant(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #Auteur du commentaire
    content = models.TextField()    #Contenu du commentaire
    restaurant = models.ForeignKey('Restaurant', null=False, on_delete=models.CASCADE) #Restaurant sur lequel on commente
    created_at = models.DateField(auto_now_add=True)    #Date de creation du commentaire
    updated_at = models.DateField(auto_now=True)    #Date de modification du commentaire


#Restaurant favoris definis par un utilisateur
class FavorisRestaurant(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #auteur qui defini ses Restaurant favoris
    restaurant = models.ForeignKey('Restaurant', null=False, on_delete=models.CASCADE) #Restaurant favoris defini par l'auteur en question