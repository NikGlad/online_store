from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),
    path('<int:id>/<slug:slug>', views.orders, name='orders'),
]