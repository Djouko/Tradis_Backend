from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# CRUD Operations Restaurant

class ListRestaurant(generics.ListAPIView):       #Read
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DetailRestaurant(generics.RetrieveUpdateAPIView):       #Update
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class CreateRestaurant(generics.CreateAPIView):       #Create
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DeleteRestaurant(generics.DestroyAPIView):      #Delete
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



# CRUD Operations FavorisRestaurant

class ListFavorisRestaurant(generics.ListAPIView):       #Read
    queryset = FavorisRestaurant.objects.all()
    serializer_class = FavorisRestaurantSerializer

class DetailFavorisRestaurant(generics.RetrieveUpdateAPIView):       #Update
    queryset = FavorisRestaurant.objects.all()
    serializer_class = FavorisRestaurantSerializer

class CreateFavorisRestaurant(generics.CreateAPIView):       #Create
    queryset = FavorisRestaurant.objects.all()
    serializer_class = FavorisRestaurantSerializer

class DeleteFavorisRestaurant(generics.DestroyAPIView):      #Delete
    queryset = FavorisRestaurant.objects.all()
    serializer_class = FavorisRestaurantSerializer


# CRUD Operations Commentaire

class ListCommentaire(generics.ListAPIView):       #Read
    queryset = CommentaireRestaurant.objects.all()
    serializer_class = CommentaireSerializer

class DetailCommentaire(generics.RetrieveUpdateAPIView):       #Update
    queryset = CommentaireRestaurant.objects.all()
    serializer_class = CommentaireSerializer

class CreateCommentaire(generics.CreateAPIView):       #Create
    queryset = CommentaireRestaurant.objects.all()
    serializer_class = CommentaireSerializer

class DeleteCommentaire(generics.DestroyAPIView):      #Delete
    queryset = CommentaireRestaurant.objects.all()
    serializer_class = CommentaireSerializer