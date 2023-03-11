from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField(max_length=255)
    is_new = models.BooleanField()
    is_discounted = models.BooleanField()
    category = models.ForeignKey(Category, CASCADE, default=None)
    brand = models.ForeignKey(Brand, CASCADE, default=None)
    image = models.ImageField(default='160Hf.png', null=True)

    def __str__(self):
        return self.title

