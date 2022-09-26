from django.db import models
from acccounts.models import User
from django.utils import timezone
from tinymce import models as tinymce_models





class Formation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identifiant = models.CharField(max_length=255)
    point_fort = tinymce_models.HTMLField()
    contenu = tinymce_models.HTMLField()
    objectif = tinymce_models.HTMLField()
    resultat_attendu = tinymce_models.HTMLField()
    #fiche = tinymce_models.HTMLField()
    update = models.DateTimeField(default=timezone.now)
    mis_a_jour = models.BooleanField(default=False)
    
    def __str__(self):
        return self.identifiant







class Blog(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='blog_pics')
    publier = models.BooleanField(default=False)
    contenu = tinymce_models.HTMLField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug, 'id': self.id}) 
    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url








class Contact(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return str(self.phone)







class FacturationMensuelle(models.Model):
    montant = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.montant) + '€'
    




class Feedback(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.auteur.email
    
    def get_absolute_url(self):
        return reverse('list_formation') #, kwargs={'slug': self.slug, 'id': self.id}) 
    