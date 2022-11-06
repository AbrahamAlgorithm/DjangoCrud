from rest_framework import generics

from .models import Song, Artiste
from .serializers import SongSerializer, ArtisteSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class  = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer    

class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class  = ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer