from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        # а также передается информация, которую заполнил пользователь
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name}({email}): {message}")
    return render(request, 'mainapp/index.html')
