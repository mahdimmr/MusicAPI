import os
from django.core.exceptions import ValidationError


def validate_music_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


def validate_cover_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

