# from django.conf.urls import url
# from . import views

from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
    path('', views.order_create, name='order_create'),
]

# from django.urls import path
# from . import views
#
# app_name = 'cart'
#
# urlpatterns = [
#     path('', views.cart_detail, name='cart_detail'),
#     path('add/<int:product_id>/',
#          views.cart_add,
#          name='cart_add'),
#     path('remove/<int:product_id>/',
#          views.cart_remove,
#          name='cart_remove'),
# ]