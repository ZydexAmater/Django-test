from django.http import Http404
from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.utils import query_search
from goods.models import Products


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale')
    order_by = request.GET.get('order_by')
    query = request.GET.get('q')

    try:
        if category_slug == 'all':
            goods = Products.objects.all()
        elif query:
            goods = query_search(query)
        else:
            goods = Products.objects.filter(category__slug=category_slug)
            if not goods.exists():
                raise Http404()

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != 'default':
            goods = goods.order_by(order_by)

        paginator = Paginator(goods, 3)
        current_page = paginator.page(int(page))

        context = {
            'goods': current_page,
            'slug_url': category_slug,
        }
        return render(request, 'goods/catalog.html', context)
    
    except Products.DoesNotExist:
        raise Http404("Category does not exist")

def cart(request):
    return render(request, 'goods/cart.html')

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product,
    }
    return render(request, 'goods/product.html', context)