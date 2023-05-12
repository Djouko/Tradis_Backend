from django.urls import path
from .views import *

urlpatterns = [
                    #Restaurant
    path('<int:pk>/', DetailRestaurant.as_view()),
    path('', ListRestaurant.as_view()),
    path('create', CreateRestaurant.as_view()),
    path('delete/<int:pk>', DeleteRestaurant.as_view()),

                    # Commentaire
    path('commentaire/<int:pk>/', DetailCommentaire.as_view()),
    path('commentaire', ListCommentaire.as_view()),
    path('commentaire/create', CreateCommentaire.as_view()),
    path('commentaire/delete/<int:pk>', DeleteCommentaire.as_view()),
                    # Favoris
    path('favoris/<int:pk>/', DetailFavorisRestaurant.as_view()),
    path('favoris', ListFavorisRestaurant.as_view()),
    path('favoris/create', CreateFavorisRestaurant.as_view()),
    path('favoris/delete/<int:pk>', DeleteFavorisRestaurant.as_view()),
]