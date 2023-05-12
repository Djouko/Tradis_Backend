from django.contrib import admin

# Register your models here.
from .models import Sites, Categories

class SitesInline(admin.TabularInline):
    model = Sites
    extra = 0

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = (SitesInline, )

@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    list_display = ('title','createdAt','updatedAt')
    list_filter = ('title','createdAt','updatedAt')
    search_fields = ('title',)