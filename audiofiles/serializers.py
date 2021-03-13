from rest_framework import serializers
from .models import Song, Podcast, Audiobook

class SongSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        max_length=len(Song.type),
        default=Song.type,
        read_only=True
    )
    class Meta:
        model = Song
        fields = Song.db_columns

class PodcastSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        max_length=len(Podcast.type),
        default=Podcast.type,
        read_only=True
    )
    class Meta:
        model = Podcast
        fields = Podcast.db_columns

class AudiobookSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        max_length=len(Audiobook.type),
        default=Audiobook.type,
        read_only=True
    )
    class Meta:
        model = Audiobook
        fields = Audiobook.db_columns