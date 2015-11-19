from .models import Video
from .models import VideoCategory

from rest_framework import serializers


class VideoCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('id', 'name')


class VideoListSerializer(serializers.ModelSerializer):
    category = VideoCategorySerializer(many=False, read_only=False)

    class Meta:
        model = Video
        fields = ('id', 'name', 'youtube_id',
        		  'description', 'category', 'status')


