from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token

from mebel_sayt.models import Category
from .forms import CategoryForm
from .servise import get_list


@staff_member_required(login_url='dash_log')
def edit_add(request, pk=None):
    forms = CategoryForm()
    if pk:
        ctg = Category.objects.get(pk=pk)
        forms = CategoryForm(instance=ctg)
    else:
        ctg = None
    if request.POST:
        if pk:
            form = CategoryForm(request.POST, instance=ctg)
        else:
            form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard_ctg_list")
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }
    return render(request, 'dashboard/category/form.html', ctx)


@staff_member_required(login_url='dash_log')
def ctg_list_detail(request, pk=None):
    token = Token.objects.get(user=request.user)
    html = ''
    ctx = {}

    if pk:
        ctg = get_list(token, pk=pk)
        ctx['ctg'] = ctg.get('item', {})
        html = 'detail'
    else:
        page = int(request.GET.get('pag', 1))

        ctgs = get_list(token.key, page=page)
        html = 'list'
        meta = ctgs.get('meta', {})
        pag = meta.get('count', 0)/meta.get('per_page', 1)
        next = page+1 if page < pag else None
        prev = page-1 if page > 1 else None

        ctx = {
            'ctgs': ctgs.get('items', {}),
            'meta': meta,
            'pag': pag + 1 if pag % 1 else pag,
            'next': next,
            'prev': prev
        }

    return render(request, f'dashboard/category/{html}.html', ctx)


@staff_member_required(login_url='dash_log')
def del_conf(request, pk=None, dlt=None):
    if dlt:
        Category.objects.get(pk=dlt).delete()
        return redirect('dashboard_ctg_list')

    ctg = Category.objects.get(pk=pk)
    ctx = {
        'ctg': ctg
    }
    return render(request, 'dashboard/category/delete.html', ctx)
