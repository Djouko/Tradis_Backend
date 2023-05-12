from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# CRUD Operations Hebergement

class ListHebergement(generics.ListAPIView):       #Read
    queryset = Hebergement.objects.all()
    serializer_class = HebergementSerializer

class DetailHebergement(generics.RetrieveUpdateAPIView):       #Update
    queryset = Hebergement.objects.all()
    serializer_class = HebergementSerializer

class CreateHebergement(generics.CreateAPIView):       #Create
    queryset = Hebergement.objects.all()
    serializer_class = HebergementSerializer

class DeleteHebergement(generics.DestroyAPIView):      #Delete
    queryset = Hebergement.objects.all()
    serializer_class = HebergementSerializer


# CRUD Operations Commentaire

class ListCommentaire(generics.ListAPIView):       #Read
    queryset = CommentaireHebergement.objects.all()
    serializer_class = CommentaireSerializer

class DetailCommentaire(generics.RetrieveUpdateAPIView):       #Update
    queryset = CommentaireHebergement.objects.all()
    serializer_class = CommentaireSerializer

class CreateCommentaire(generics.CreateAPIView):       #Create
    queryset = CommentaireHebergement.objects.all()
    serializer_class = CommentaireSerializer

class DeleteCommentaire(generics.DestroyAPIView):      #Delete
    queryset = CommentaireHebergement.objects.all()
    serializer_class = CommentaireSerializer



#Recherche d'un site touristique par le lieu
class HebergementSearchLieu(generics.ListAPIView):
    serializer_class = HebergementSearchLieuSerializer

    def get_queryset(self):
        lieu_slug = self.kwargs['lieu_slug']
        #lieu = Categories.objects.get(lieu=lieu_slug)
        queryset = Hebergement.objects.filter(lieu=lieu_slug)
        return queryset


# CRUD Operations FavorisHebergement

class ListFavorisHebergement(generics.ListAPIView):       #Read
    queryset = FavorisHebergement.objects.all()
    serializer_class = FavorisHebergementSerializer

class DetailFavorisHebergement(generics.RetrieveUpdateAPIView):       #Update
    queryset = FavorisHebergement.objects.all()
    serializer_class = FavorisHebergementSerializer

class CreateFavorisHebergement(generics.CreateAPIView):       #Create
    queryset = FavorisHebergement.objects.all()
    serializer_class = FavorisHebergementSerializer

class DeleteFavorisHebergement(generics.DestroyAPIView):      #Delete
    queryset = FavorisHebergement.objects.all()
    serializer_class = FavorisHebergementSerializer