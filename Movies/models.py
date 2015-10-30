from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.


class Genre(models.Model):
    """
        Model for Category mapping
    """
    category = models.CharField(max_length=255, default=None, blank=True, null= True)


class Movies(models.Model):
    """
        Model for storing Movies data
    """
    name = models.CharField(max_length=255, default=None, blank=True, null= True)
    director = models.CharField(max_length=255, default=None, blank=True, null= True)
    popularity = models.FloatField(blank=True, null=True)
    imdb_score = models.FloatField(blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)