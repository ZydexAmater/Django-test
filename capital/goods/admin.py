from django.contrib import admin
from .models import Products, Categories

# Register your models here.


#admin.site.register(Products)
#admin.site.register(Categories)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
