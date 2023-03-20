from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80)


class Product(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Review(models.Model):
    text = models.CharField(max_length=150)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


