from rest_framework import serializers
from .models import *

class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ('id','nom','description','photo','tarif','contact')

class LocationVehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationVehicule
        fields = ('id','nom','lieu','description','photo','tarif','Disponibilite')

class AgenceVoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenceVoyage
        fields = ('id','nom','lieu','description','photo')

class ItineraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itineraire
        fields = ('id','nom','tarif','agence')



class CommentaireTaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireTaxi
        fields = '__all__'


class FavorisTaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavorisTaxi
        fields = ('id','author','taxi')


class CommentaireLocationVehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireLocationVehicule
        fields = '__all__'


class FavorisLocationVehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavorisLocationVehicule
        fields = ('id','author','locationVehicule')



class CommentaireAgenceVoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireAgenceVoyage
        fields = '__all__'


class FavorisAgenceVoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavorisAgenceVoyage
        fields = ('id','author','agenceVoyage')