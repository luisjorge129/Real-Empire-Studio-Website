from .models import Teacher
from .models import Class

from rest_framework import serializers


class TeacherSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'slug')


class ClassSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField('get_teachers_list')
    start_time = serializers.TimeField(format='%-I:%M%p',
                                       required=False, read_only=True)
    end_time = serializers.TimeField(format='%-I:%M%p',
                                      required=False, read_only=True)

    def get_teachers_list(self, course):
        try:
            if course:
              queryset = Teacher.objects.filter(status=True,
                                                course__pk=course.pk)
              serializer = TeacherSimpleSerializer(instance=queryset,
                                                   many=True)
              return serializer.data
        except Teacher.DoesNotExist:
            return None

    class Meta:
        model = Class
        fields = ('id', 'name', 'slug',
                  'day', 'start_time',
                  'end_time', 'teachers')


class TeacherSerializer(serializers.ModelSerializer):
    course = ClassSerializer(many=True, read_only=True)
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
        model = Teacher
        fields = ('id', 'name', 'slug',
                  'biography', 'image_thumbnail',
                  'image_small', 'image_medium',
                  'image_large', 'image_full',
                  'facebook',  'twitter',
                  'google_plus', 'instagram',
                  'course')
