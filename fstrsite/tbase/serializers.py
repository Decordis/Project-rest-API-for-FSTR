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

    def validate(self, data):
        if self.instance is not None:
            if self.instance.status != 'NW':
                raise serializers.ValidationError(
                    f'Отказ! Причина: статус {self.instance.get_status_display()}'
                )

        user = self.instance.user_id
        user_data = data.get('user_id')
        user_fields = [
            user.full_name != user_data['full_name'],
            user.email != user_data['email'],
            user.phone != user_data['phone'],
        ]

        if user_data is not None and any(user_fields):
            raise serializers.ValidationError(
                f'Отклонено! Нельзя менять данные пользователя'
            )
        return data
