from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.base),
    path('product', views.product),
]