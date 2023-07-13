from rest_framework import serializers
from mebel_sayt.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



