from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token

from mebel_sayt.models import Product
from .forms import ProductForm
from .servise import get_list


@staff_member_required(login_url='dash_log')
def prod_add_edit(request, pk=None):
    forms = ProductForm()
    if pk:
        ctg = Product.objects.get(pk=pk)
        forms = ProductForm(instance=ctg)
    else:
        ctg = None
    if request.POST:
        if pk:
            form = ProductForm(request.POST, request.FILES or None, instance=ctg)
        else:
            form = ProductForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect("dashboard_prod_list")
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }
    return render(request, 'dashboard/product/form.html', ctx)


@staff_member_required(login_url='dash_log')
def prod_list(request):
    token = Token.objects.get(user=request.user)

    page = int(request.GET.get('pag', 1))

    ctgs = get_list(token.key, page=page)
    meta = ctgs.get('meta', {})
    pag = meta.get('count', 0) / meta.get('per_page', 1)
    next = page + 1 if page < pag else None
    prev = page - 1 if page > 1 else None

    ctx = {
        'ctgs': ctgs.get('items', {}),
        'meta': meta,
        'pag': pag + 1 if pag % 1 else pag,
        'next': next,
        'prev': prev
    }
    return render(request, 'dashboard/product/list.html', ctx)


@staff_member_required(login_url='dash_log')
def prod_detail(request, pk):
    ctg = Product.objects.get(pk=pk)
    ctx = {
        'ctg': ctg
    }
    return render(request, 'dashboard/product/detail.html', ctx)


@staff_member_required(login_url='dash_log')
def prod_del_conf(request, pk):
    ctg = Product.objects.get(pk=pk)
    ctx = {
        'ctg': ctg
    }
    return render(request, 'dashboard/product/delete.html', ctx)


@staff_member_required(login_url='dash_log')
def prod_delete(request, pk):
    ctg = Product.objects.get(pk=pk).delete()
    return redirect('dashboard_prod_list')
