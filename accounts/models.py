from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='India')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_image',null=True, blank=True)

    India = UserProfileManager()
    objects = models.Manager()
    
    def __str__(self):
        return self.user.username

