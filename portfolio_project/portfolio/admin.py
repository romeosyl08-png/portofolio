from django.contrib import admin
from .models import Competence, Projet, Experience

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie', 'niveau', 'ordre']
    list_editable = ['ordre']
    list_filter = ['categorie']

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ['titre', 'featured', 'date_creation']
    list_filter = ['featured']
    prepopulated_fields = {}

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['titre', 'organisation', 'type_experience', 'date_debut', 'en_cours']
    list_filter = ['type_experience']