from goods.models import Products
from django.db.models import Q


def query_search(query):
    if query.isdigit() and len(query) > 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2]

    query_objects = Q()

    for keyword in keywords:
        query_objects |= Q(name__icontains=keyword) | Q(description__icontains=keyword)

    return Products.objects.filter(query_objects)