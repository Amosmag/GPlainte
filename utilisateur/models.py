from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


from os.path import splitext, basename

from django.db import models

from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.conf import settings


class PictureStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'location': settings.MEDIA_ROOT,
            'base_url': settings.MEDIA_URL
        })
        super(PictureStorage, self).__init__(*args, **kwargs)


def upload_path(instance, filename):
    filename = basename(filename)
    _, extension = splitext(filename)
    now = timezone.now()
    prefix = 'photo'
    return '{}/{}/{}'.format(
        prefix, now.year, extension)


class User(AbstractUser):
    profession = models.CharField(max_length=150, null=True, verbose_name='profession')
    fonction = models.CharField(max_length=200, null=True, verbose_name='fonction')
    photo_name = models.CharField(max_length=100, null=True, verbose_name='photo_name')
    photo = models.ImageField(upload_to='images/photos/', null=True)
    nom_prenoms = models.CharField(max_length=100, null=True, verbose_name='nom et prenoms')
    #photo = models.ImageField(upload_to=upload_path, null=True, storage=PictureStorage(), verbose_name='photo')

    pass


# Create your models here.
