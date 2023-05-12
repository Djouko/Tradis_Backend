from rest_framework import serializers
from .models import *

class ActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = ('id','nom','lieu','description','latitude','longitude','photos','videos','Date_Evenement','Evenement_payant','prix')



class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireActivite
        fields = '__all__'


class FavorisActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavorisActivite
        fields = ('id','author','activite')