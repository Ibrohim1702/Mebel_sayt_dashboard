from django.shortcuts import render
from rest_framework.templatetags.rest_framework import data

from .models import Product, Category, ProductImg


def get_images(pro):
    return ProductImg.objects.filter(product=pro)


def index(request):
    queryset = Product.objects.all()
    l = []
    for i in queryset:
        l.append({"products": i, "img": [x for x in get_images(i)]})

    ctx = {
        'products': l

    }

    return render(request, 'sayt/index.html', ctx)


def contacts(request):
    ctx = {
    }
    return render(request, 'sayt/contacts.html', ctx)


def product(request, pk=None, slug=None):
    if slug:
        product1 = Category.objects.get(slug=slug)
        product2 = Product.objects.filter(product1=product1)
        ctx = {
            'product3': product2
        }
        return render(request, 'sayt/product.html', ctx)
    elif pk:
        product = Product.objects.all()
        new = Product.objects.get(pk=pk)
        imgs = ProductImg.objects.filter(new=new)
        ctx = {
            "new": new,
            'product': product,
            'imgs': imgs
        }
        return render(request, ctx)

    return render(request, 'sayt/product.html')


def catalog(request, slug=None, pk=None):
    if slug:
        ctg = Category.objects.get(slug=slug)
        prod_list = Product.objects.filter(ctg=ctg)
        ctx = {
            'products': prod_list
        }
    else:
        products = Product.objects.all()
        l = []
        for i in products:
            l.append({"products": i, "img": [x for x in get_images(i)]})
        ctx = {
            "products": l
        }

    return render(request, 'sayt/catalog.html', ctx)


def cart(request):
    ctx = {

    }
    return render(request, 'sayt/cart.html')


def swatches(request):
    ctx = {

    }
    return render(request, 'sayt/swatches.html')


def warranty(request):
    ctx = {
    }
    return render(request, 'sayt/warranty.html')


def view(request, pk):
    product = Product.objects.get(pk=pk)
    imgs = ProductImg.objects.filter(product=product)
    ctx = {
        "product": product,
        'imgs': imgs
    }
    return render(request, 'sayt/view.html', ctx)
