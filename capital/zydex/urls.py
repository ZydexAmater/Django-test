from django.urls import path
from zydex import views

app_name = 'zydex'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories')
]
