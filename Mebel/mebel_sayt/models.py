from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    content = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)

        return super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.CharField(max_length=64)
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=128)
    material = models.CharField(max_length=128)
    fillIn = models.CharField(max_length=128)
    is_bed = models.BooleanField(default=False)
    wide = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    bed_length = models.IntegerField(null=True, blank=True)
    bed_wide = models.IntegerField(null=True, blank=True)
    bed_height = models.IntegerField(null=True, blank=True)
    to_bot = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductImg(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='images')

    def __str__(self):
        return self.product.name
