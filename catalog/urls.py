from django.urls import path

from catalog.views import home, contacts, product
from catalog import apps

app_name = apps.CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product_info')
]
