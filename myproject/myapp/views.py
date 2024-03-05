from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Group


# Create your views her

@login_required
def student_dashboard(request):
    # Это представление будет доступно только студентам
    return render(request, 'student_dashboard.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        group = Group.objects.filter(number=user).first()

        if group is not None:
            login(request, user)
            # Перенаправить пользователя на другую страницу после входа
            return redirect('student_dashboard')
        else:
            # В случае неудачной аутентификации показать сообщение об ошибке
            error_message = "Неверное имя пользователя или пароль"
            return render(request, 'student_login.html', {'error_message': error_message})
    else:
        # Возвращаем пустую страницу или другое представление
        return render(request, 'student_login.html')