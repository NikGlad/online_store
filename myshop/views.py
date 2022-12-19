from django.shortcuts import render, redirect
from django.urls import path
from . import views
from django.http import HttpResponse

def base(request): #создаём функцию
    return render(request, 'shop/base.html') # в кавычках отбражаем ссылка на HTML. то что будет отображаться
# вместо HttpResponse используем метод render


def product(request):
    return render(request, 'shop/product/detail.html')
