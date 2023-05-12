from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# CRUD Operations Sites

class ListSite(generics.ListAPIView):       #Read
    queryset = Sites.objects.all()
    serializer_class = SiteSerializer

class DetailSite(generics.RetrieveUpdateAPIView):       #Update
    queryset = Sites.objects.all()
    serializer_class = SiteSerializer

class CreateSite(generics.CreateAPIView):       #Create
    queryset = Sites.objects.all()
    serializer_class = SiteSerializer

class DeleteSite(generics.DestroyAPIView):      #Delete
    queryset = Sites.objects.all()
    serializer_class = SiteSerializer

# CRUD Operations Sites Categories

class ListSiteCategories(generics.ListAPIView):       #Read
    queryset = Categories.objects.all()
    serializer_class = SiteCategoriesSerializer

class DetailSiteCategories(generics.RetrieveUpdateAPIView):       #Update
    queryset = Categories.objects.all()
    serializer_class = SiteCategoriesSerializer

class CreateSiteCategories(generics.CreateAPIView):       #Create
    queryset = Categories.objects.all()
    serializer_class = SiteCategoriesSerializer

class DeleteSiteCategories(generics.DestroyAPIView):      #Delete
    queryset = Categories.objects.all()
    serializer_class = SiteCategoriesSerializer


#Recherche d'un site touristique par l'id de la category
class SiteSearchCategory(generics.ListAPIView):
    serializer_class = SiteSearchCategorySerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = Categories.objects.get(id=category_slug)
        queryset = Sites.objects.filter(list=category)
        return queryset

#Recherche d'un site touristique par le lieu
class SiteSearchLieu(generics.ListAPIView):
    serializer_class = SiteSearchLieuSerializer

    def get_queryset(self):
        lieu_slug = self.kwargs['lieu_slug']
        #lieu = Categories.objects.get(lieu=lieu_slug)
        queryset = Sites.objects.filter(lieu=lieu_slug)
        return queryset

#Recherche d'un site touristique avec local guide
class SiteSearchLocalGuide(generics.ListAPIView):
    serializer_class = SiteSearchLocalGuideSerializer
    queryset = Sites.objects.filter(local_guide_available=False)

#Recherche d'un site touristique gratuit
class SiteSearchFree(generics.ListAPIView):
    serializer_class = SiteSearchFreeSerializer
    queryset = Sites.objects.filter(prix=0.0)



# CRUD Operations Commentaire

class ListCommentaire(generics.ListAPIView):       #Read
    queryset = CommentaireSite.objects.all()
    serializer_class = CommentaireSerializer

class DetailCommentaire(generics.RetrieveUpdateAPIView):       #Update
    queryset = CommentaireSite.objects.all()
    serializer_class = CommentaireSerializer

class CreateCommentaire(generics.CreateAPIView):       #Create
    queryset = CommentaireSite.objects.all()
    serializer_class = CommentaireSerializer

class DeleteCommentaire(generics.DestroyAPIView):      #Delete
    queryset = CommentaireSite.objects.all()
    serializer_class = CommentaireSerializer


# CRUD Operations FavorisSite

class ListFavorisSite(generics.ListAPIView):       #Read
    queryset = FavorisSite.objects.all()
    serializer_class = FavorisSiteSerializer

class DetailFavorisSite(generics.RetrieveUpdateAPIView):       #Update
    queryset = FavorisSite.objects.all()
    serializer_class = FavorisSiteSerializer

class CreateFavorisSite(generics.CreateAPIView):       #Create
    queryset = FavorisSite.objects.all()
    serializer_class = FavorisSiteSerializer

class DeleteFavorisSite(generics.DestroyAPIView):      #Delete
    queryset = FavorisSite.objects.all()
    serializer_class = FavorisSiteSerializer




#Gestion des locals guide
class LocalGuideList(generics.ListCreateAPIView):
    serializer_class = LocalGuideSerializer

    def get_queryset(self):
        site_id = self.kwargs['site_id']
        return LocalGuide.objects.filter(site_id=site_id)

    def perform_create(self, serializer):
        site_id = self.kwargs['site_id']
        site = Sites.objects.get(id=site_id)
        serializer.save(site=site)
        site.local_guide_available = True
        site.save()

    def perform_update(self, serializer):
        site_id = self.kwargs['site_id']
        site = Sites.objects.get(id=site_id)
        serializer.save(site=site)
        if site.local_guides.filter(available=True).exists():
            site.local_guide_available = True
        else:
            site.local_guide_available = False
        site.save()

class LocalGuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocalGuide.objects.all()
    serializer_class = LocalGuideSerializer

    def perform_destroy(self, instance):
        site = instance.site
        instance.delete()
        if site.local_guides.filter(available=True).exists():
            site.local_guide_available = True
        else:
            site.local_guide_available = False
        site.save()