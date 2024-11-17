from django.shortcuts import render

from goods.models import Products


def catalog(requests):
    products = Products.objects.all()
    context = {
        'products': products,
        #'categories': categories,
    }
    return render(requests, 'goods/catalog.html', context)

def cart(requests):
    return render(requests, 'goods/cart.html')

def product(requests, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product,
    }
    return render(requests, 'goods/product.html', context)