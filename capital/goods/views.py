from django.shortcuts import render # type: ignore
from django.core.paginator import Paginator

from goods.models import Products


def catalog(requests, category_slug):
    page = requests.GET.get('page', 1)
    
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'goods': current_page,
        'slug_url': category_slug,
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