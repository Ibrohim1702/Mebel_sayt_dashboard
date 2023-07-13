from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("contacts/", contacts, name='contacts'),
    path("product/", product, name='product'),
    path("catalog/", catalog, name='catalog'),
    path("catalog/<slug>/", catalog, name='catalog_one'),
    path('product/<int:pk>/', product, name='product_one'),
    path('product/<slug>/', product, name='product_two'),
    path('cart', cart, name='cart'),
    path('swatches/', swatches, name='swatches'),
    path('warranty/', warranty, name='warranty'),
    path("view/<int:pk>/", view, name='product_view')
]
