from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

@csrf_exempt
@staff_member_required
def corbeille(request):
    if request.method == 'GET':
        # récupérer le type de ressource sélectionné dans la requête GET
        resource_type = request.GET.get('resource_type')

        # récupérer les ressources supprimées pour le type de ressource sélectionné
        content_type = ContentType.objects.get(model=resource_type)
        deleted_resources = content_type.model_class()._base_manager.filter(deleted=True)

        # filtrer les ressources supprimées par administrateur, date de suppression et chaîne de caractères
        admin_username = request.GET.get('admin_username')
        if admin_username:
            deleted_resources = deleted_resources.filter(deleted_by__username=admin_username)
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date and end_date:
            start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = timezone.datetime.strptime(end_date, '%Y-%m-%d').date()
            deleted_resources = deleted_resources.filter(deleted_at__range=[start_date, end_date])
        search_query = request.GET.get('search_query')
        if search_query:
            deleted_resources = deleted_resources.filter(name__icontains=search_query)

        # renvoyer la liste des ressources supprimées
        response_data = []
        for resource in deleted_resources:
            resource_data = {
                'id': resource.id,
                'name': resource.name,
                'deleted_by': resource.deleted_by.username,
                'deleted_at': resource.deleted_at,
            }
            response_data.append(resource_data)
        return JsonResponse({'deleted_resources': response_data})

@csrf_exempt
@staff_member_required
def restaurer_ressource(request, resource_id):
    if request.method == 'POST':
        try:
            # restaurer la ressource avec l'ID spécifié
            content_type = ContentType.objects.get_for_id(request.POST.get('content_type_id'))
            model_class = content_type.model_class()
            resource = model_class.objects.get(id=resource_id)
            resource.deleted = False
            resource.save()
            return JsonResponse({'success': True})
        except Exception as e:
            # renvoyer une erreur si la restauration échoue
            return JsonResponse({'success': False, 'error': str(e)})




#Ce code définit deux vues pour les deux actions spécifiées : corbeille pour afficher la liste des ressources supprimées et restaurer_ressource pour restaurer une ressource supprimée. Ces vues utilisent le décorateur @csrf_exempt pour permettre les requêtes POST sans avoir à inclure un token CSRF dans chaque requête. Le décorateur @staff_member_required assure que seuls les utilisateurs ayant les droits d'administrateur peuvent accéder à ces vues.

#La vue corbeille récupère le type de ressource sélectionné dans la requête GET et utilise le modèle ContentType de Django pour trouver le modèle correspondant. Elle filtre ensuite les ressources supprimées pour le type de ressource sélectionné et les filtre davantage selon les critères spécifiés dans la requête GET. Elle renvoie enfin une réponse JSON contenant une liste des ressources supprimées correspondantes.

#La vue restaurer_ressource récupère l'ID de la ressource à restaurer à partir de l'URL de la requête. Elle utilise ensuite le modèle ContentType pour trouver le modèle de la ressource correspondante. Elle restaure ensuite la ressource en définissant la valeur deleted sur False et renvoie une réponse JSON indiquant si la restauration a réussi ou a échoué, ainsi qu'un message d'erreur si applicable.

