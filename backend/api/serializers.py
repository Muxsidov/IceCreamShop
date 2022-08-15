from rest_framework import serializers

from .models import IceCream

class IceCreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = [
            'title',
            'content',
            'price',
            'instore'
        ]