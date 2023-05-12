from django.contrib.auth.models import User
from django.db import models
# from multiupload.fields import MultiFileField
# from django import forms

class Activite(models.Model):
    nom = models.CharField(max_length=255)  #Nom de l'activite
    lieu = models.CharField(max_length=255) #Lieu de l'activite
    description = models.TextField(blank=True)  #Description de l'activite
    photos = models.ImageField(upload_to='public', blank=True, null=True)   #Photo de presentation de l'activite
    videos = models.FileField(upload_to='videos/')  #Video de presentation de l'activite
    Date_Evenement = models.DateField(blank=False)  # Date de l'événement
    Evenement_payant = models.BooleanField(default=True)    #Dire si l'evenement est payant ou non
    prix = models.DecimalField(max_digits=5, decimal_places=2, default=0.0) #Prix de l'evenemet
    latitude = models.FloatField(null=True)  # Longitude pour la localisation du lieu d'une activite
    longitude = models.FloatField(null=True)  # Latitude pour la localisation du lieu d'une activite

    def __str__(self):
        return self.nom



#Commentaires laisses par les utilisateurs sur une Activite
class CommentaireActivite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #Auteur du commentaire
    content = models.TextField()    #Contenu du commentaire
    activite = models.ForeignKey('Activite', null=False, on_delete=models.CASCADE) #Activite sur lequel on commente
    created_at = models.DateField(auto_now_add=True)    #Date de creation du commentaire
    updated_at = models.DateField(auto_now=True)    #Date de modification du commentaire


#Activite favoris definis par un utilisateur
class FavorisActivite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #auteur qui defini ses Activites favoris
    activite = models.ForeignKey('Activite', null=False, on_delete=models.CASCADE) #Activite favoris defini par l'auteur en question