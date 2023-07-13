from django.contrib import admin
from .models import User


admin.site.register(User)
# from django.contrib import admin
# from .models import Category, Product, ProductImg
#
#
# class ProImg(admin.StackedInline):
#     model = ProductImg
#
#
# class ProImgAdmin(admin.ModelAdmin):
#     inlines = [ProImg]
#
#
