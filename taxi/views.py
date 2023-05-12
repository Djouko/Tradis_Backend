from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# CRUD Operations Taxi

class ListTaxi(generics.ListAPIView):       #Read
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer

class DetailTaxi(generics.RetrieveUpdateAPIView):       #Update
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer

class CreateTaxi(generics.CreateAPIView):       #Create
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer

class DeleteTaxi(generics.DestroyAPIView):      #Delete
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer


# CRUD Operations LocationVehicule

class ListLocationVehicule(generics.ListAPIView):       #Read
    queryset = LocationVehicule.objects.all()
    serializer_class = LocationVehiculeSerializer

class DetailLocationVehicule(generics.RetrieveUpdateAPIView):       #Update
    queryset = LocationVehicule.objects.all()
    serializer_class = LocationVehiculeSerializer

class CreateLocationVehicule(generics.CreateAPIView):       #Create
    queryset = LocationVehicule.objects.all()
    serializer_class = LocationVehiculeSerializer

class DeleteLocationVehicule(generics.DestroyAPIView):      #Delete
    queryset = LocationVehicule.objects.all()
    serializer_class = LocationVehiculeSerializer


# CRUD Operations AgenceVoyage

class ListAgenceVoyage(generics.ListAPIView):       #Read
    queryset = AgenceVoyage.objects.all()
    serializer_class = AgenceVoyageSerializer

class DetailAgenceVoyage(generics.RetrieveUpdateAPIView):       #Update
    queryset = AgenceVoyage.objects.all()
    serializer_class = AgenceVoyageSerializer

class CreateAgenceVoyage(generics.CreateAPIView):       #Create
    queryset = AgenceVoyage.objects.all()
    serializer_class = AgenceVoyageSerializer

class DeleteAgenceVoyage(generics.DestroyAPIView):      #Delete
    queryset = AgenceVoyage.objects.all()
    serializer_class = AgenceVoyageSerializer



# CRUD Operations Itineraire

class ListItineraire(generics.ListAPIView):       #Read
    queryset = Itineraire.objects.all()
    serializer_class = ItineraireSerializer

class DetailItineraire(generics.RetrieveUpdateAPIView):       #Update
    queryset = Itineraire.objects.all()
    serializer_class = ItineraireSerializer

class CreateItineraire(generics.CreateAPIView):       #Create
    queryset = Itineraire.objects.all()
    serializer_class = ItineraireSerializer

class DeleteItineraire(generics.DestroyAPIView):      #Delete
    queryset = Itineraire.objects.all()
    serializer_class = ItineraireSerializer





# CRUD Operations FavorisTaxi

class ListFavorisTaxi(generics.ListAPIView):       #Read
    queryset = FavorisTaxi.objects.all()
    serializer_class = FavorisTaxiSerializer

class DetailFavorisTaxi(generics.RetrieveUpdateAPIView):       #Update
    queryset = FavorisTaxi.objects.all()
    serializer_class = FavorisTaxiSerializer

class CreateFavorisTaxi(generics.CreateAPIView):       #Create
    queryset = FavorisTaxi.objects.all()
    serializer_class = FavorisTaxiSerializer

class DeleteFavorisTaxi(generics.DestroyAPIView):      #Delete
    queryset = FavorisTaxi.objects.all()
    serializer_class = FavorisTaxiSerializer


# CRUD Operations Commentaire Taxi

class ListCommentaireTaxi(generics.ListAPIView):       #Read
    queryset = CommentaireTaxi.objects.all()
    serializer_class = CommentaireTaxiSerializer

class DetailCommentaireTaxi(generics.RetrieveUpdateAPIView):       #Update
    queryset = CommentaireTaxi.objects.all()
    serializer_class = CommentaireTaxiSerializer

class CreateCommentaireTaxi(generics.CreateAPIView):       #Create
    queryset = CommentaireTaxi.objects.all()
    serializer_class = CommentaireTaxiSerializer

class DeleteCommentaireTaxi(generics.DestroyAPIView):      #Delete
    queryset = CommentaireTaxi.objects.all()
    serializer_class = CommentaireTaxiSerializer



# CRUD Operations FavorisLocationVehicule

class ListFavorisLocationVehicule(generics.ListAPIView):       #Read
    queryset = FavorisLocationVehicule.objects.all()
    serializer_class = FavorisLocationVehiculeSerializer

class DetailFavorisLocationVehicule(generics.RetrieveUpdateAPIView):       #Update
    queryset = FavorisLocationVehicule.objects.all()
    serializer_class = FavorisLocationVehiculeSerializer

class CreateFavorisLocationVehicule(generics.CreateAPIView):       #Create
    queryset = FavorisLocationVehicule.objects.all()
    serializer_class = FavorisLocationVehiculeSerializer

class DeleteFavorisLocationVehicule(generics.DestroyAPIView):      #Delete
    queryset = FavorisLocationVehicule.objects.all()
    serializer_class = FavorisLocationVehiculeSerializer


# CRUD Operations Commentaire LocationVehicule

class ListCommentaireLocationVehicule(generics.ListAPIView):       #Read
    queryset = CommentaireLocationVehicule.objects.all()
    serializer_class = CommentaireLocationVehiculeSerializer

class DetailCommentaireLocationVehicule(generics.RetrieveUpdateAPIView):       #Update
    queryset = CommentaireLocationVehicule.objects.all()
    serializer_class = CommentaireLocationVehiculeSerializer

class CreateCommentaireLocationVehicule(generics.CreateAPIView):       #Create
    queryset = CommentaireLocationVehicule.objects.all()
    serializer_class = CommentaireLocationVehiculeSerializer

class DeleteCommentaireLocationVehicule(generics.DestroyAPIView):      #Delete
    queryset = CommentaireLocationVehicule.objects.all()
    serializer_class = CommentaireLocationVehiculeSerializer




# CRUD Operations FavorisAgenceVoyage

class ListFavorisAgenceVoyage(generics.ListAPIView):       #Read
    queryset = FavorisAgenceVoyage.objects.all()
    serializer_class = FavorisAgenceVoyageSerializer

class DetailFavorisAgenceVoyage(generics.RetrieveUpdateAPIView):       #Update
    queryset = FavorisAgenceVoyage.objects.all()
    serializer_class = FavorisAgenceVoyageSerializer

class CreateFavorisAgenceVoyage(generics.CreateAPIView):       #Create
    queryset = FavorisAgenceVoyage.objects.all()
    serializer_class = FavorisAgenceVoyageSerializer

class DeleteFavorisAgenceVoyage(generics.DestroyAPIView):      #Delete
    queryset = FavorisAgenceVoyage.objects.all()
    serializer_class = FavorisAgenceVoyageSerializer


# CRUD Operations Commentaire AgenceVoyage

class ListCommentaireAgenceVoyage(generics.ListAPIView):       #Read
    queryset = CommentaireAgenceVoyage.objects.all()
    serializer_class = CommentaireAgenceVoyageSerializer

class DetailCommentaireAgenceVoyage(generics.RetrieveUpdateAPIView):       #Update
    queryset = CommentaireAgenceVoyage.objects.all()
    serializer_class = CommentaireAgenceVoyageSerializer

class CreateCommentaireAgenceVoyage(generics.CreateAPIView):       #Create
    queryset = CommentaireAgenceVoyage.objects.all()
    serializer_class = CommentaireAgenceVoyageSerializer

class DeleteCommentaireAgenceVoyage(generics.DestroyAPIView):      #Delete
    queryset = CommentaireAgenceVoyage.objects.all()
    serializer_class = CommentaireAgenceVoyageSerializer