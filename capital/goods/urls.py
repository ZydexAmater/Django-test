from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.categories, name='product'),
    path('cart/', views.cart, name='cart')
]
