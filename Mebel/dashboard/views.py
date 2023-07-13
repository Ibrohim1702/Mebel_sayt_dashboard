from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token

from dashboard.forms import DashboardUserForm
from dashboard.models import User
from dashboard.servise import edit_profile


def index(request):
    user = request.user
    if user.is_anonymous:
        return redirect('dash_login')

    ctx = {
        'user': user,
        'home': True
    }

    return render(request, "dashboard/base.html", ctx)


def register(request):
    if request.POST:
        password = request.POST.get('pass')
        password_conf = request.POST.get('pass_conf')
        username = request.POST.get('username')
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        if password_conf != password:
            return redirect('dash_register')

        user = User()
        user.user_name = username
        user.name = name
        user.phone = phone
        user.set_password(password)
        user.save()
        Token.objects.create(user)

        user = authenticate(request, user_name=username, password=password)
        login(request, user)
        return redirect("dashboardHome")
    return render(request, 'dashboard/register.html')


def dash_login(request):
    ctx = {
        'error': False
    }
    if request.POST:
        password = request.POST.get('pass')
        username = request.POST.get('username')

        user = User.objects.filter(user_name=username).first()
        if not user:
            ctx = {
                'error': True
            }
            return render(request, 'dashboard/login.html', ctx)
        if user.check_password(password):
            user = authenticate(request, user_name=username, password=password)
            login(request, user)
            return redirect("dashboardHome")
        else:
            ctx = {
                'error': True
            }

    return render(request, 'dashboard/login.html', ctx)


def dash_logout(request):
    user = request.user
    if user.is_anonymous:
        return redirect('dash_login')
    logout(request)
    return redirect('dash_login')


def edit_user(request):
    user = request.user
    if user.is_anonymous:
        return redirect('dash_login')

    data = {}
    if request.POST:
        for i in request.POST:
            data[i] = request.POST.get(i)

        try:
            token = Token.objects.get(user=request.user)
        except:
            token = Token.objects.create(user=request.user)

        response = edit_profile(data, token.key)
        print(response)
        return redirect('dash_user_edit')

    ctx = {
        'user': user
    }

    return render(request, "dashboard/user.html", ctx)


def change_password(request):
    user = request.user
    if user.is_anonymous:
        return redirect('dashboard_login')

    if request.POST:
        old = request.POST.get('old')
        password = request.POST.get('pass')
        password_conf = request.POST.get('pass_conf')
        user = User.objects.get(id=request.user.id)

        if not user.check_password(old):
            return redirect('dash_user_change_password')

        if password and password_conf and password_conf != password:
            return redirect('dash_user_change_password')

        user.set_password(password)
        user.save()
        user = authenticate(request, user_name=user.user_name, password=password)
        login(request, user)
        return redirect('dashboardHome')
    return render(request, 'dashboard/pass_change.html')
