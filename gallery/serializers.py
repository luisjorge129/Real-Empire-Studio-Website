from .models import Video
from .models import VideoCategory

from rest_framework import serializers


class VideoCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoCategory
        fields = ('id', 'name')


class VideoListSerializer(serializers.ModelSerializer):
    category = VideoCategorySerializer(many=False, read_only=False)

    class Meta:
        model = Video
        fields = ('id', 'name', 'video_id', 'video_type',
                  'description', 'category', 'status')
