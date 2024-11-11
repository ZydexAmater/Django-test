from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.product, name='product'),
    path('cart/', views.cart, name='cart')
]
