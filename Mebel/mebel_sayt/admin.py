from django.contrib import admin
from .models import Category, Product, ProductImg


class ProImg(admin.StackedInline):
    model = ProductImg


class ProImgAdmin(admin.ModelAdmin):
    inlines = [ProImg]


admin.site.register(Category)
admin.site.register(Product, ProImgAdmin)
