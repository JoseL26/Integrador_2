from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from lista.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    Imagen = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.Imagen:
            return '{}{}'.format(MEDIA_URL, self.Imagen)
        return '{}{}'.format(STATIC_URL, 'imagen/empity.png')