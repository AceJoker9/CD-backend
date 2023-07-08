from rest_framework import serializers
from .models import Tracks

class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields =['id', 'title', 'album', 'release_date', 'genre']