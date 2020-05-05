from rest_framework import serializers
from apps.api.models import Jokes


class JokeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jokes
        fields = ('id', 'joke', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')