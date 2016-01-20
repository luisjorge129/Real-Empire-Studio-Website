from .models import Video
from .models import VideoCategory
from .models import Gallery
from .models import GalleryCategory

from rest_framework import serializers


class VideoCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoCategory
        fields = ('id', 'name')


class VideoListSerializer(serializers.ModelSerializer):
    category = VideoCategorySerializer(many=True, read_only=False)

    class Meta:
        model = Video
        fields = ('id', 'name', 'video_id', 'video_type',
                  'description', 'category', 'status')


class GalleryCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GalleryCategory
        fields = ('id', 'name')


class GalleryListSerializer(serializers.ModelSerializer):
    category = GalleryCategorySerializer(many=True, read_only=False)
    image_thumbnail = serializers.SerializerMethodField('get_image_thumbnail_url')
    image_small = serializers.SerializerMethodField('get_image_small_url')
    image_medium = serializers.SerializerMethodField('get_image_medium_url')
    image_large = serializers.SerializerMethodField('get_image_large_url')
    image_full = serializers.SerializerMethodField('get_image_full_url')

    def get_image_thumbnail_url(self, obj):
        return obj.image_small.url

    def get_image_small_url(self, obj):
        return obj.image_small.url

    def get_image_medium_url(self, obj):
        return obj.image_medium.url

    def get_image_large_url(self, obj):
        return obj.image_large.url

    def get_image_full_url(self, obj):
        return obj.image.url

    def get_image_url(self, obj):
        return obj.image_medium.url

    class Meta:
        model = Gallery
        fields = ('id', 'name', 'description', 'image_thumbnail',
                  'image_small', 'image_medium',
                  'image_large', 'image_full', 'category',
                  'status')
