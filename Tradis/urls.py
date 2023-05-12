"""Tradis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include('sites.urls')),
    path('api/activite/', include('Activite.urls')),
    path('api/hebergement/', include('Hebergement.urls')),
    path('api/restaurant/', include('restaurant.urls')),
    path('api/taxi/', include('taxi.urls')),
                #Corbeille **
    path('corbeille/', views.corbeille, name='corbeille'),
    path('corbeille/<str:resource_type>/<int:resource_id>/restaurer/', views.restaurer_ressource, name='restaurer_ressource'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# **
#Ces deux routes associées à leur vue respectives permettent d'accéder aux fonctionnalités définies dans les vues corbeille et restaurer_ressource.

#La première route 'corbeille/' associe la vue corbeille à l'URL /corbeille/, ce qui permet d'afficher la liste des ressources supprimées.

#La deuxième route 'corbeille/<str:resource_type>/<int:resource_id>/restaurer/' associe la vue restaurer_ressource à l'URL /corbeille/<type_de_ressource>/<id_de_la_ressource>/restaurer/, ce qui permet de restaurer une ressource supprimée. Notez que <str:resource_type> et <int:resource_id> sont des paramètres d'URL qui seront passés à la vue restaurer_ressource.