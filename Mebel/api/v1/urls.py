from django.urls import path
from api.v1.mebel_sayt.category.views import CategoryView
from api.v1.mebel_sayt.product.views import ProductView
from api.v1.dashboard.user.views import RegisterApi, LoginApi, UpdateUser

urlpatterns = [
    path('mebel_sayt/ctg/', CategoryView.as_view(), name='api_ctg_list'),
    path('mebel_sayt/ctg/page-<int:page>/', CategoryView.as_view(), name='api_ctg_list'),
    path('mebel_sayt/ctg/<int:pk>/', CategoryView.as_view(), name='api_ctg_one'),


    path('mebel_sayt/prod/', ProductView.as_view(), name='api_prod_list'),
    path('mebel_sayt/prod/<int:pk>/', ProductView.as_view(), name='api_prod_one'),


    path('dashboard/register/', RegisterApi.as_view(), name='api_dashboard_register'),
    path('dashboard/login/', LoginApi.as_view(), name='api_dashboard_login'),
    path('dashboard/user/', UpdateUser.as_view(), name='api_dashboard_user_update')

]


