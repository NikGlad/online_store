from django.shortcuts import render, get_object_or_404
from .models import Product, Basket
from cart.forms import CartAddProductForm


def product_list(request):
    products = Product.objects.filter(available=True)

    return render(request, 'shop/product/list.html',
                  {
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

def orders(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/orders/orders.html', {'product': product,
                                                        'cart_product_form': cart_product_form})