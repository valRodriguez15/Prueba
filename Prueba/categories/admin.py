from django.contrib import admin
from categories.models import Tours, Activities

@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ['user', 'nombre', 'disponibilidad']

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'miniature']
