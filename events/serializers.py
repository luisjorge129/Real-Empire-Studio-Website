from .models import Event

from rest_framework import serializers


class EventListSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%d/%m/%Y %H:%M',
                                     required=False, read_only=True)
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

    class Meta:
        model = Event
        fields = ('id', 'name', 'slug',
                  'description', 'time',
                  'image', 'image_thumbnail',
                  'image_small', 'image_medium',
                  'image_large', 'image_full',
                  'facebook', 'twitter',
                  'google_plus')
