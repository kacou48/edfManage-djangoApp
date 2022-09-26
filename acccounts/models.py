from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
from django.utils import timezone
from datetime import timedelta



#elle herite de abstractUser. username es desactivé , email doit etre unique et
#un champ obligatoire.
class User(AbstractUser):

    is_email_verified = models.BooleanField(default=False)
    accepter = models.BooleanField(default=False, blank=False, null=False)
    
    username = None
    email = models.EmailField(unique=True, null=False, blank=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



class Userprofile(models.Model):
    ACTIF = 'actif'
    INACTIF = 'inactif'
    STATUS = (
        (ACTIF, 'actif'),
       (INACTIF, 'inactif')
    )
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default=INACTIF)

    image = models.ImageField(default='profile.png', upload_to='profile_pics')
    
    def __str__(self):
        return self.user.email


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class LesAbonnee(models.Model):
    user = models.OneToOneField(User, related_name='abonnee', on_delete=models.CASCADE)
    debut =  models.DateTimeField(default=timezone.now)
    fin = models.DateTimeField()

    def __str__(self):
        return self.user.email

    
    def save(self, *args, **kwargs):
        
        self.fin = self.debut + timedelta(days=31)
        super().save(*args, **kwargs)

     

