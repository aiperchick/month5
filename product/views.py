from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, RatingSerializer
from . import models, serializers


@api_view(['GET'])
def products_reviews_rating_view(request):
    products = Product.objects.all()
    serializer = RatingSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        category = models.Category.objects.create(name=name)
        return Response(data=serializers.CategorySerializer(category).data)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        categories = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found!'})
    if request.method == 'GET':
        serializer = serializers.CategorySerializer(categories)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        categories.name = request.data.get('name')
        return Response(data=serializers.CategorySerializer(categories).data)
    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category = request.data.get('category')
        product = models.Product.objects.create(name=title, description=description, price=price, category=category)
        product.category.set(category)
        product.save()
        return Response(data=serializers.ProductSerializer(product).data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product does not exist'})
    if request.method == 'GET':
        serializer = serializers.ProductSerializer(product)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        category = request.data.get('category')
        product.category.set(category)
        product.save()
        return Response(data=serializers.ProductSerializer(product).data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        product = request.data.get('product')
        stars = request.data.get('stars')
        review = models.Review.objects.create(text=text, product=product, stars=stars)
        return Response(data=serializers.ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        reviews = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review does not exist!'})
    if request.method == 'GET':
        serializer = serializers.ReviewSerializer(reviews)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.product = request.data.get('product')
        reviews.stars = request.data.get('stars')
        return Response(data=serializers.ReviewSerializer(reviews).data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
