from django.db import models


# Create your models here.

class Log(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    message = models.JSONField(default={'state': 0})

    def __str__(self):
        return "#%s" % self.user_id


class TgUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True, null=False)
    user_name = models.CharField(max_length=256, null=True)
    lang = models.IntegerField(null=True)
    subscribe = models.BooleanField(default=False)
    kurs = models.CharField(max_length=15, null=True)


class Category(models.Model):
    name_uz = models.CharField(max_length=56)
    name_ru = models.CharField(max_length=56)

    def __str__(self):
        return self.name_uz


class Sub(models.Model):
    name = models.CharField(max_length=256)
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=128)
    til = models.IntegerField(default=1)
    ctg = models.ForeignKey(Sub, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
