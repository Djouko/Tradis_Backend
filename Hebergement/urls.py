from django.urls import path
from .views import *

urlpatterns = [
                    #Hergement
    path('<int:pk>/', DetailHebergement.as_view()),
    path('', ListHebergement.as_view()),
    path('create', CreateHebergement.as_view()),
    path('delete/<int:pk>', DeleteHebergement.as_view()),

                    #Hebergement search
    path('lieu/<str:lieu_slug>/',HebergementSearchLieu.as_view()),   #Rechercher les sites en fonction du lieu

                    # Commentaire
    path('commentaire/<int:pk>/', DetailCommentaire.as_view()),
    path('commentaire', ListCommentaire.as_view()),
    path('commentaire/create', CreateCommentaire.as_view()),
    path('commentaire/delete/<int:pk>', DeleteCommentaire.as_view()),
                    # Favoris
    path('favoris/<int:pk>/', DetailFavorisHebergement.as_view()),
    path('favoris', ListFavorisHebergement.as_view()),
    path('favoris/create', CreateFavorisHebergement.as_view()),
    path('favoris/delete/<int:pk>', DeleteFavorisHebergement.as_view()),
]