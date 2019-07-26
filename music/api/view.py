from django.forms import model_to_dict
from rest_framework import viewsets
from music.models import *
from .serializers import MusicSerializer
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def get_queryset(self):
        if self.request.query_params.get('text', None) is not None:
            text = self.request.query_params.get('text', None)
            musics = Music.objects.filter(lyric__contains=text)
            if musics.__len__() == 0:
                raise NotFound
            return musics

        else:
            return Music.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        file_url = request.build_absolute_uri(instance.file.url)
        cover_url = request.build_absolute_uri(instance.cover.url)

        instance = model_to_dict(instance)
        instance["file"] = file_url
        instance["cover"] = cover_url
        return Response(instance)


@api_view(["GET"])
def stream_music(request):
    print("\n\n\n")
    print(request)
