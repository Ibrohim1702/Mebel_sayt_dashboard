from collections import OrderedDict

from mebel_sayt.models import ProductImg
from collections import OrderedDict

from Mebel.settings import PER_PAGE
from base.sqlpaginator import SqlPaginator
from mebel_sayt.models import Product


def prod_pag(requests):
    ctgs = Product.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page-1) * limit

    result = []
    for i in range(offset, offset+limit):
        try:
            result.append(prod_format(ctgs[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(ctgs))
    meta = pagging.get_paginated_response()
    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_prod(data):

    return OrderedDict([
        ("items", prod_format(data))
    ])


def prod_format(data):

    imgs = ProductImg.objects.filter(product=data)
    img = [x.img.path for x in imgs]
    return OrderedDict([
        ('id', data.id),
        ('name', data.name),
        ('ctg_id', data.ctg.id),
        ('ctg_content', data.ctg.content),
        ('ctg_slug', data.ctg.slug),
        ('img', img),
        ("price", data.price),
        ("color", data.color),
        ("material", data.material),
        ("fillIn", data.fillIn),
        ("is_bed", data.is_bed),
        ("wide", data.wide),
        ("height", data.height),
        ("bed_length", data.bed_length),
        ("bed_wide", data.bed_wide),
        ("bed_height", data.bed_height)
    ])
