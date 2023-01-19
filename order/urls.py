from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.order, name='order'),
    path('add/<int:product_id>/',
         views.order_add,
         name='order_add'),
    path('remove/<int:product_id>/',
         views.order_remove,
         name='order_remove'),
]