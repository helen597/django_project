from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductForm(forms.ModelForm):
    # Наследуемся от специального класса форм, который предоставляет
    # весь необходимый функционал, который нужно настроить
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', )


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def contacts(request):
#     if request.method == 'POST':
#         # в переменной request хранится информация о методе, который отправлял пользователь
#         name = request.POST.get('name')
#         # а также передается информация, которую заполнил пользователь
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"{name}({phone}): {message}")
#     return render(request, 'catalog/contacts.html')
