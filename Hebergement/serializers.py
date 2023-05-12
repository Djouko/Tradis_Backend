from rest_framework import serializers
from .models import *

class HebergementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hebergement
        fields = ('id','nom','lieu','nature','description','latitude','longitude','photo','video','Tarification','Disponibilite','nombre_piece')


class HebergementSearchLieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hebergement
        fields = '__all__'


class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireHebergement
        fields = '__all__'


class FavorisHebergementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavorisHebergement
        fields = ('id','author','hebergement')