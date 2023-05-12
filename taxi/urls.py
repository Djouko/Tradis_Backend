from django.urls import path
from .views import *

urlpatterns = [
                    #Taxi
    path('<int:pk>/', DetailTaxi.as_view()),
    path('', ListTaxi.as_view()),
    path('create', CreateTaxi.as_view()),
    path('delete/<int:pk>', DeleteTaxi.as_view()),
                    #LocationVehicule
    path('locationvehicule/<int:pk>/', DetailLocationVehicule.as_view()),
    path('locationvehicule', ListLocationVehicule.as_view()),
    path('locationvehicule/create', CreateLocationVehicule.as_view()),
    path('locationvehicule/delete/<int:pk>', DeleteLocationVehicule.as_view()),
                            #AgenceVoyage
    path('agencevoyage/<int:pk>/', DetailAgenceVoyage.as_view()),
    path('agencevoyage', ListAgenceVoyage.as_view()),
    path('agencevoyage/create', CreateAgenceVoyage.as_view()),
    path('agencevoyage/delete/<int:pk>', DeleteAgenceVoyage.as_view()),
                            #Itineraire
    path('itineraire/<int:pk>/', DetailItineraire.as_view()),
    path('itineraire', ListItineraire.as_view()),
    path('itineraire/create', CreateItineraire.as_view()),
    path('itineraire/delete/<int:pk>', DeleteItineraire.as_view()),

                    # Commentaire   Taxi
    path('taxi/commentaire/<int:pk>/', DetailCommentaireTaxi.as_view()),
    path('taxi/commentaire', ListCommentaireTaxi.as_view()),
    path('taxi/commentaire/create', CreateCommentaireTaxi.as_view()),
    path('taxi/commentaire/delete/<int:pk>', DeleteCommentaireTaxi.as_view()),
                    # Favoris   Taxi
    path('taxi/favoris/<int:pk>/', DetailFavorisTaxi.as_view()),
    path('taxi/favoris', ListFavorisTaxi.as_view()),
    path('taxi/favoris/create', CreateFavorisTaxi.as_view()),
    path('taxi/favoris/delete/<int:pk>', DeleteFavorisTaxi.as_view()),

                    # Commentaire   LocationVehicule
    path('locationVehicule/commentaire/<int:pk>/', DetailCommentaireLocationVehicule.as_view()),
    path('locationVehicule/commentaire', ListCommentaireLocationVehicule.as_view()),
    path('locationVehicule/commentaire/create', CreateCommentaireLocationVehicule.as_view()),
    path('locationVehicule/commentaire/delete/<int:pk>', DeleteCommentaireLocationVehicule.as_view()),
                    # Favoris   LocationVehicule
    path('locationVehicule/favoris/<int:pk>/', DetailFavorisLocationVehicule.as_view()),
    path('locationVehicule/favoris', ListFavorisLocationVehicule.as_view()),
    path('locationVehicule/favoris/create', CreateFavorisLocationVehicule.as_view()),
    path('locationVehicule/favoris/delete/<int:pk>', DeleteFavorisLocationVehicule.as_view()),

                    # Commentaire   AgenceVoyage
    path('agenceVoyage/commentaire/<int:pk>/', DetailCommentaireAgenceVoyage.as_view()),
    path('agenceVoyage/commentaire', ListCommentaireAgenceVoyage.as_view()),
    path('agenceVoyage/commentaire/create', CreateCommentaireAgenceVoyage.as_view()),
    path('agenceVoyage/commentaire/delete/<int:pk>', DeleteCommentaireAgenceVoyage.as_view()),
                    # Favoris   AgenceVoyage
    path('agenceVoyage/favoris/<int:pk>/', DetailFavorisAgenceVoyage.as_view()),
    path('agenceVoyage/favoris', ListFavorisAgenceVoyage.as_view()),
    path('agenceVoyage/favoris/create', CreateFavorisAgenceVoyage.as_view()),
    path('agenceVoyage/favoris/delete/<int:pk>', DeleteFavorisAgenceVoyage.as_view()),
]