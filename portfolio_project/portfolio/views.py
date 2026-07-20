from django.shortcuts import render
from .models import Competence, Projet, Experience

def portfolio_view(request):
    context = {
        'competences': Competence.objects.all(),
        'projets': Projet.objects.all(),
        'experiences': Experience.objects.all(),
        'projets_featured': Projet.objects.filter(featured=True),
    }
    return render(request, 'portfolio/portfolio.html', context)