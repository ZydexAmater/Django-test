from django.shortcuts import render # type: ignore

from goods.models import Products


def catalog(requests, catalog_slug):
    if catalog_slug == 'all':
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__slug=catalog_slug)
        
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