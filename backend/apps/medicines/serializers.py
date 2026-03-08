from rest_framework import serializers
from .models import Medicine, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MedicineSerializer(serializers.ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Medicine
        fields = "__all__"