from django.urls import path
from .views import *
from dashboard.category import views as ctg_views
from dashboard.product import views as prod_views
urlpatterns = [
    path("", index, name='dashboardHome'),
    path("category/", ctg_views.ctg_list_detail, name='dashboard_ctg_list'),
    path("category/<int:pk>", ctg_views.ctg_list_detail, name='dash_ctg_detail'),
    path("ctg/delete/<int:dlt>", ctg_views.del_conf, name='dash_ctg_delete'),
    path("ctg/conf/<int:pk>", ctg_views.del_conf, name='dash_ctg_conf'),
    path("category/add", ctg_views.edit_add, name='dash_ctg_add'),
    path("category/edit/<int:pk>", ctg_views.edit_add, name='dash_ctg_edit'),

    path("product/", prod_views.prod_list, name='dashboard_prod_list'),
    path("product/<int:pk>", prod_views.prod_detail, name='dash_prod_detail'),
    path("product/conf/<int:pk>", prod_views.prod_del_conf, name='dash_prod_conf'),
    path("product/delete/<int:pk>", prod_views.prod_delete, name='dash_prod_delete'),
    path("product/add", prod_views.prod_add_edit, name='dash_prod_add'),
    path("product/edit/<int:pk>/", prod_views.prod_add_edit, name='dash_prod_edit'),

    path("register/", register, name='dash_register'),
    path("login/", dash_login, name='dash_login'),
    path("logout/", dash_logout, name='dash_logout'),
    path("user/", edit_user, name='dash_user_edit'),
    path("user/change_pass", change_password, name='dash_user_change_password'),
]

