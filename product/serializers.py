from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name products_count'.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title price description category_name'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id stars product_name'.split()


class RatingSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = models.Product
        fields = 'id title reviews rating'.split()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=80)
    description = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.ListField(child=serializers.IntegerField())

    def validate_category(self, category):
        try:
            Category.objects.get(id=category)
        except Category.DoesNotExist:
            raise ValidationError('category not found!')
        return category


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=80)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_product(self, product):
        try:
            Product.objects.get(id=product)
        except Product.DoesNotExist:
            raise ValidationError('product not found!')
        return product
