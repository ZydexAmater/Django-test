from django.shortcuts import render

# Create your views here.


def categories(requests):
    return render(requests, 'goods/product.html')

def cart(requests):
    return render(requests, 'goods/cart.html')