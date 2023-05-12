from django.urls import path
from .views import *

urlpatterns = [
                    #Sites
    path('<int:pk>/', DetailSite.as_view()),    #Affiche les details d'un site touristique par son identifiant
    path('', ListSite.as_view()),   #Liste les sites touristiques
    path('create', CreateSite.as_view()),   #Creer un site touristique
    path('delete/<int:pk>', DeleteSite.as_view()),  #Supprimer un site touristique
    path('sites/<int:site_id>/local_guides/', LocalGuideList.as_view(), name='local-guide-list'),
    path('local_guides/<int:pk>/', LocalGuideDetail.as_view(), name='local-guide-detail'),

                    #Sites Categories
    path('categories/<int:pk>/', DetailSiteCategories.as_view()),   #Affiche les details d'une categorie de site touristique par son identifiant
    path('categories', ListSiteCategories.as_view()),   #Liste les categories de site touristique
    path('categories/create', CreateSiteCategories.as_view()),  #Creer une categorie de site touristique
    path('categories/delete/<int:pk>', DeleteSiteCategories.as_view()), #Supprimer une categorie de site touristique
                    #Site Search
    path('sites/category/<int:category_slug>/',SiteSearchCategory.as_view()),   #Rechercher les sites en fonction de la categorie
    path('sites/lieu/<str:lieu_slug>/',SiteSearchLieu.as_view()),   #Rechercher les sites en fonction du lieu
    path('sites/localguide/',SiteSearchLocalGuide.as_view()),   #Rechercher les sites qui ont un local guide
    path('sites/free/',SiteSearchFree.as_view()),   #rechercher les sites qui sont gratuits
                    # Commentaire
    path('commentaire/<int:pk>/', DetailCommentaire.as_view()),
    path('commentaire', ListCommentaire.as_view()),
    path('commentaire/create', CreateCommentaire.as_view()),
    path('commentaire/delete/<int:pk>', DeleteCommentaire.as_view()),
                    # Favoris
    path('favorissite/<int:pk>/', DetailFavorisSite.as_view()),
    path('favorissite', ListFavorisSite.as_view()),
    path('favorissite/create', CreateFavorisSite.as_view()),
    path('favorissite/delete/<int:pk>', DeleteFavorisSite.as_view()),
]