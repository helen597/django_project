from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_price(value):
    if value <= 0:
        raise ValidationError(
            _("Цена %(value)s должна быть положительным целым числом"),
            params={"value": value},
        )


# Create your models here.
class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(validators=[validate_price], verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    # manufactured_at = models.DateField(verbose_name='Дата производства продукта', null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=300, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)
