from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import RestaurantMenu


class RestaurantMenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = "__all__"


class RestaurantMenuDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = ["restaurant_name", "ratind"]


class RestaurantMenuRatingSerializer(serializers.Serializer):
    rating = serializers.FloatField()

    def validate_rating(self, value):
        if value > 10:
            raise ValidationError("Some custom error")
        if value < 0:
            raise ValidationError
