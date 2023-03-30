from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    @property
    def products_count(self):
        return self.products.count()


class Product(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    category = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.title

    @property
    def rating(self):
        stars_list = [review.stars for review in self.reviews.all()]
        return round(sum(stars_list) / len(stars_list), 2)

    @property
    def category_name(self):
        categories = [category.name for category in self.category.all()]
        return categories


class Review(models.Model):
    STARS = ((i, '* ' * i) for i in range(1, 6))
    text = models.CharField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, null=True)

    def __str__(self):
        return self.text

    @property
    def product_name(self):
        return self.product.title
