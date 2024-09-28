from rest_framework import serializers
from .models import PointAdd


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