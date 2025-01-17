from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True, validators=[validate_email])
    superfan_of = models.ForeignKey('heroes.Superhero', on_delete=models.SET_NULL, null=True, blank=True, related_name='superfans')
    fan_of = models.ManyToManyField('heroes.Superhero', related_name='fans', blank=True)
    

    def __str__(self):
        return self.username