from rest_framework import generics
from apps.api.serializers import JokeSerializer
from apps.api.models import Jokes


class CreateJoke(generics.ListCreateAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokeSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Jokes.objects.all()
    serializer_class = JokeSerializer