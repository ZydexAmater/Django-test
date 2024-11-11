from django.shortcuts import render

from goods.models import Products

# Create your views here.

products = Products.objects.all()
categories = Products.objects.all()

def product(requests):
    context = {
        'products': products,
        'categories': categories,
    }
    return render(requests, 'goods/product.html', context)

def cart(requests):
    return render(requests, 'goods/cart.html')