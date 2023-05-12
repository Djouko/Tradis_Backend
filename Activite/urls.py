from django.urls import path
from .views import *

urlpatterns = [
                    #Sites
    path('<int:pk>/', DetailActivite.as_view()),
    path('', ListActivite.as_view()),
    path('create', CreateActivite.as_view()),
    path('delete/<int:pk>', DeleteActivite.as_view()),

                    # Commentaire
    path('commentaire/<int:pk>/', DetailCommentaire.as_view()),
    path('commentaire', ListCommentaire.as_view()),
    path('commentaire/create', CreateCommentaire.as_view()),
    path('commentaire/delete/<int:pk>', DeleteCommentaire.as_view()),
                    # Favoris
    path('favoris/<int:pk>/', DetailFavorisActivite.as_view()),
    path('favoris', ListFavorisActivite.as_view()),
    path('favoris/create', CreateFavorisActivite.as_view()),
    path('favoris/delete/<int:pk>', DeleteFavorisActivite.as_view()),
]