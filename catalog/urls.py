from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView
from catalog import apps

app_name = apps.CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product')
]
