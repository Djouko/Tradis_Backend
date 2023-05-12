from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# CRUD Operations Activite

class ListActivite(generics.ListAPIView):       #Read
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer

class DetailActivite(generics.RetrieveUpdateAPIView):       #Update
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer

class CreateActivite(generics.CreateAPIView):       #Create
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer

class DeleteActivite(generics.DestroyAPIView):      #Delete
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer


# CRUD Operations FavorisActivite

class ListFavorisActivite(generics.ListAPIView):       #Read
    queryset = FavorisActivite.objects.all()
    serializer_class = FavorisActiviteSerializer

class DetailFavorisActivite(generics.RetrieveUpdateAPIView):       #Update
    queryset = FavorisActivite.objects.all()
    serializer_class = FavorisActiviteSerializer

class CreateFavorisActivite(generics.CreateAPIView):       #Create
    queryset = FavorisActivite.objects.all()
    serializer_class = FavorisActiviteSerializer

class DeleteFavorisActivite(generics.DestroyAPIView):      #Delete
    queryset = FavorisActivite.objects.all()
    serializer_class = FavorisActiviteSerializer


# CRUD Operations Commentaire

class ListCommentaire(generics.ListAPIView):       #Read
    queryset = CommentaireActivite.objects.all()
    serializer_class = CommentaireSerializer

class DetailCommentaire(generics.RetrieveUpdateAPIView):       #Update
    queryset = CommentaireActivite.objects.all()
    serializer_class = CommentaireSerializer

class CreateCommentaire(generics.CreateAPIView):       #Create
    queryset = CommentaireActivite.objects.all()
    serializer_class = CommentaireSerializer

class DeleteCommentaire(generics.DestroyAPIView):      #Delete
    queryset = CommentaireActivite.objects.all()
    serializer_class = CommentaireSerializer