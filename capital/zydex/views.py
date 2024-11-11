from django.shortcuts import render
from goods.models import Products, Categories
# Create your views here.

def index(requests):
    categories = Categories.objects.all()
    products = Products.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }

    return render(requests, 'zydex/index.html', context)

def about(requests):
    return render(requests, 'zydex/about.html')
