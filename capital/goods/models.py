from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название') 
    slug = models.SlugField(max_length=150, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    quantity = models.PositiveBigIntegerField(default=0, verbose_name='Количество')
    discount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, verbose_name='Скидка')
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    
    def __str__(self):
        return self.name

    def product_id(self):
        return f'{self.id:005}'
    
    def get_discount_price(self):
        return f"{self.price - (self.price * self.discount / 100):.2f}"