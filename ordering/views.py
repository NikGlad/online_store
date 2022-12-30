from django.shortcuts import render, get_object_or_404


def ordering(request): #создаём функцию
    return render(request, "shop/ordering/ordering.html")