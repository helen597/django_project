from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    context = {'object_list': Product.objects.all()}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        # а также передается информация, которую заполнил пользователь
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name}({phone}): {message}")
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'object': product}
    return render(request, 'catalog/product.html', context)
