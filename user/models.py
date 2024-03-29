from crum import get_current_request
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.forms import model_to_dict

from lista.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    Imagen = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.Imagen:
            return '{}{}'.format(MEDIA_URL, self.Imagen)
        return '{}{}'.format(STATIC_URL, 'imagen/empity.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['Imagen'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name}for g in self.groups.all()]
        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass

