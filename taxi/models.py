from django.contrib.auth.models import User
from django.db import models

class Taxi(models.Model):
    nom = models.CharField(max_length=255)  #Nom du taxi
    description = models.TextField(blank=True)  #Description du taxi
    photo = models.ImageField(upload_to='public', blank=True, null=True)    #Photo de presentation du taxi
    tarif = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)    #Tarif par heure du taxi
    contact = models.CharField(max_length=15)   #Contact du proprietaire du taxi

    def __str__(self):
        return self.nom

class LocationVehicule(models.Model):
    nom = models.CharField(max_length=255)  #Nom du vehicule a louer
    lieu = models.CharField(max_length=255) #Lieu de l'agence
    description = models.TextField(blank=True)  #Description du vehicule a louer
    photo = models.ImageField(upload_to='public', blank=True, null=True) #Photo de presentation du vehicule a louer
    tarif = models.DecimalField(max_digits=8, decimal_places=4, default=0.0)    #Tarif par jour du vehicule a louer
    Disponibilite = models.BooleanField(default=True)   #Disponibilite du vehicule a louer

    def __str__(self):
        return self.nom


class AgenceVoyage(models.Model):
    nom = models.CharField(max_length=255)  #Nom de l'agence de voyage
    lieu = models.CharField(max_length=255) #Lieu de l'agence de voyage
    description = models.TextField(blank=True)  #Description de l'agence de voyage
    photo = models.ImageField(upload_to='public', blank=True, null=True)    #Photo de presentation de l'agence de voyage

    def __str__(self):
        return self.nom

class Itineraire(models.Model):
    nom = models.CharField(max_length=100)  #Nom de l'itineraire couvert par l'agence
    tarif = models.DecimalField(max_digits=8, decimal_places=4, default=0.0)    #Tarif de l'itineraire couvert par l'agence
    agence = models.ForeignKey(AgenceVoyage, on_delete=models.CASCADE, related_name='itineraire')   #Agence correspondant a l'itineraire

    def __str__(self):
        return self.nom


#Commentaires laisses par les utilisateurs sur un Taxi
class CommentaireTaxi(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #Auteur du commentaire
    content = models.TextField()    #Contenu du commentaire
    taxi = models.ForeignKey('Taxi', null=False, on_delete=models.CASCADE) #Taxi sur lequel on commente
    created_at = models.DateField(auto_now_add=True)    #Date de creation du commentaire
    updated_at = models.DateField(auto_now=True)    #Date de modification du commentaire


#Activite favoris definis par un utilisateur
class FavorisTaxi(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #auteur qui defini ses Taxi favoris
    taxi = models.ForeignKey('Taxi', null=False, on_delete=models.CASCADE) #Taxi favoris defini par l'auteur en question



#Commentaires laisses par les utilisateurs sur une LocationVehicule
class CommentaireLocationVehicule(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #Auteur du commentaire
    content = models.TextField()    #Contenu du commentaire
    locationVehicule = models.ForeignKey('LocationVehicule', null=False, on_delete=models.CASCADE) #LocationVehicule sur lequel on commente
    created_at = models.DateField(auto_now_add=True)    #Date de creation du commentaire
    updated_at = models.DateField(auto_now=True)    #Date de modification du commentaire


#Activite favoris definis par un utilisateur
class FavorisLocationVehicule(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #auteur qui defini ses LocationVehicule favoris
    locationVehicule = models.ForeignKey('LocationVehicule', null=False, on_delete=models.CASCADE) #LocationVehicule favoris defini par l'auteur en question




#Commentaires laisses par les utilisateurs sur un AgenceVoyage
class CommentaireAgenceVoyage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #Auteur du commentaire
    content = models.TextField()    #Contenu du commentaire
    agenceVoyage = models.ForeignKey('AgenceVoyage', null=False, on_delete=models.CASCADE) #AgenceVoyage sur lequel on commente
    created_at = models.DateField(auto_now_add=True)    #Date de creation du commentaire
    updated_at = models.DateField(auto_now=True)    #Date de modification du commentaire


#Activite favoris definis par un utilisateur
class FavorisAgenceVoyage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #auteur qui defini ses AgenceVoyage favoris
    agenceVoyage = models.ForeignKey('AgenceVoyage', null=False, on_delete=models.CASCADE) #AgenceVoyage favoris defini par l'auteur en question
