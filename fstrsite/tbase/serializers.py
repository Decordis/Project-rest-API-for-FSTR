from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
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


class PointAddSerializer(WritableNestedModelSerializer):
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
            'status',
        )

    def validate(self, attrs):
        if attrs.get('status') != 'NW':
            raise serializers.ValidationError("Вы не можете изменить данный пост.")

        if attrs.get('user_id'):
            raise serializers.ValidationError("Данный пользователь уже существует!.")
        return attrs
