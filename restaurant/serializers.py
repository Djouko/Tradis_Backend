from rest_framework import serializers
from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','nom','lieu','description','photo','latitude','longitude')



class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireRestaurant
        fields = '__all__'


class FavorisRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavorisRestaurant
        fields = ('id','author','restaurant')