from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from config import settings

NULLABLE = {'null': True, 'blank': True}

def validate_price(value):
    if value <= 0:
        raise ValidationError(
            _("Цена %(value)s должна быть положительным целым числом"),
            params={"value": value},
        )


# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(validators=[validate_price], verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    # manufactured_at = models.DateField(verbose_name='Дата производства продукта', null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=300, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Version(models.Model):

    number = models.IntegerField(default=1, verbose_name='Номер')
    name = models.CharField(max_length=100, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Текущая')
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return f'{self.number}: {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('number',)
