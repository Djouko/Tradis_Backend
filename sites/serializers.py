from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ('id','title','lieu','description','latitude','longitude','informations','attachement','video','local_guide_available','prix','createdAt','updatedAt','categorie')

class SiteCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id','name')

class SiteSearchCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ('id','title','lieu','description','latitude','longitude','informations','attachement','video','local_guide_available','prix','createdAt','updatedAt','categorie')

class SiteSearchLieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ('id','title','lieu','description','latitude','longitude','informations','attachement','video','local_guide_available','prix','createdAt','updatedAt','categorie')

class SiteSearchLocalGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ('id','title','lieu','description','latitude','longitude','informations','attachement','video','local_guide_available','prix','createdAt','updatedAt','categorie')

class SiteSearchFreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ('id','title','lieu','description','latitude','longitude','informations','attachement','video','local_guide_available','prix','createdAt','updatedAt','categorie')

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireSite
        fields = ('id','content','author','site','created_at','updated_at')

class FavorisSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavorisSite
        fields = ('id','author','site')



class LocalGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalGuide
        fields = '__all__'