from rest_framework import serializers
from music.models import *


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ("url", "name", "artist", "duration")

