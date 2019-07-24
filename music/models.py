from django.db import models
import random
import os
from music.api.validators import validate_cover_file, validate_music_file


def rename_music(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for x in range(10))

    return 'uploads/musics/{random_string}{extension}'.format(basename=base_filename,
                                                              random_string=random_str,
                                                              extension=file_extension)


def rename_cover(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for x in range(10))

    return 'uploads/covers/{random_string}{extension}'.format(basename=base_filename,
                                                              random_string=random_str,
                                                              extension=file_extension)


class Music(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file = models.FileField(upload_to=rename_music, validators=[validate_music_file])
    cover = models.ImageField(upload_to=rename_cover, validators=[validate_cover_file])
    duration = models.CharField(max_length=255)
    lyric = models.TextField()
