from abc import ABC

from rest_framework import serializers
from .models import Item, Review


class ReviewSerializer(serializers.Serializer):
    grade = serializers.IntegerField(required=True, min_value=1, max_value=10)
    text = serializers.CharField(required=True, max_length=1024)


class ItemSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=64)
    description = serializers.CharField(required=True, max_length=1024)
    price = serializers.IntegerField(required=True, min_value=1, max_value=1000000)
