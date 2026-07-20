from django.db import models

class Competence(models.Model):
    CATEGORIE_CHOICES = [
        ('backend', 'Backend'),
        ('mecatronique', 'Mécatronique'),
        ('cybersecurite', 'Cybersécurité'),
        ('autre', 'Autre'),
    ]
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    niveau = models.IntegerField(help_text="Pourcentage de 0 à 100")
    icone = models.CharField(max_length=50, help_text="Ex: fab fa-python (FontAwesome)")
    description_courte = models.CharField(max_length=150)
    description_longue = models.TextField()
    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return self.nom


class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description_courte = models.CharField(max_length=200)
    description_longue = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Séparées par des virgules")
    image = models.ImageField(upload_to='projets/', blank=True, null=True)
    lien_github = models.URLField(blank=True)
    lien_demo = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    date_creation = models.DateField()

    class Meta:
        ordering = ['-date_creation']

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',')]

    def __str__(self):
        return self.titre


class Experience(models.Model):
    TYPE_CHOICES = [
        ('formation', 'Formation'),
        ('projet', 'Projet'),
        ('experience', 'Expérience'),
    ]
    titre = models.CharField(max_length=200)
    organisation = models.CharField(max_length=200)
    type_experience = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    en_cours = models.BooleanField(default=False)
    description = models.TextField()

    class Meta:
        ordering = ['-date_debut']

    def __str__(self):
        return f"{self.titre} - {self.organisation}"