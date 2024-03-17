from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    # Наследуемся от специального класса форм, который предоставляет
    # весь необходимый функционал, который нужно настроить
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', )