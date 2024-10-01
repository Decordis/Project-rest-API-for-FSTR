from rest_framework import serializers
from .models import PointAdd, Image, Users, Coord, LevelPoint


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'full_name',
            'email',
            'phone',
        )


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = (
            'latitude',
            'longitude',
            'height',
        )


class LevelPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelPoint
        fields = (
            'winter_level',
            'spring_level',
            'summer_level',
            'autumn_level',
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'title',
            'img',
        )


class PointAddSerializer(serializers.ModelSerializer):
    user_id = UsersSerializer()
    coord_id = CoordSerializer()
    level = LevelPointSerializer()
    photo_img = ImageSerializer()

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
            'level',
            'photo_img',
        )
