from collections import OrderedDict

from Mebel.settings import PER_PAGE
from base.sqlpaginator import SqlPaginator
from mebel_sayt.models import Category


def ctg_pag(requests):
    ctgs = Category.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page-1) * limit

    result = []
    for i in range(offset, offset+limit):
        try:
            result.append(ctg_format(ctgs[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(ctgs))
    meta = pagging.get_paginated_response()
    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_ctg(data):

    return OrderedDict([
        ("items", ctg_format(data))
    ])


def ctg_format(data):
    return OrderedDict([
        ('id', data.id),
        ('content', data.content),
        ('slug', data.slug),
    ])
