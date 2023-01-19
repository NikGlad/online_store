from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myshop.models import Product
from .order import Order
from .forms import OrderAddProductForm


@require_POST
def order_add(request, product_id):
    order = Order(request)
    product = get_object_or_404(Product, id=product_id)
    form = OrderAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        order.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('order:order')


def order_remove(request, product_id):
    order = Order(request)
    product = get_object_or_404(Product, id=product_id)
    order.remove(product)
    return redirect('order:order')


def order(request):
    order = Order(request)
    for item in order:
        item['update_quantity_form'] = OrderAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'shop/order/order.html', {'order': order})
