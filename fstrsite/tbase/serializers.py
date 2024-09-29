from rest_framework import serializers
from .models import PointAdd, Image, Users


class PointAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointAdd
        fields = (
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'date',
            'coord_id',
            'user_id',
            'photo_img',
            'status',
            'winter_level',
            'spring_level',
            'summer_level',
            'autumn_level',
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        photo_img = serializers.URLField()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'full_name',
            'email',
            'phone',
        )

