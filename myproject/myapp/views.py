from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Group, Record, File


# Create your views her

@login_required
def student_dashboard(request):
    group_records = Record.objects.filter(group=request.user.group)

    # # Получаем все файлы, прикрепленные к каждой записи
    # for record in group_records:
    #     files = File.objects.filter(record=record)
    #     record.files = files

    return render(request, 'student_dashboard.html', {'group_records': group_records})


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


def logout_view(request):
    logout(request)
    # Перенаправить пользователя на другую страницу после выхода
    return redirect('student_login')  # Замените 'student_login' на имя URL вашей страницы входа для студентов


def group_records(request, group_id):
    group_records = Record.objects.filter(group_id=group_id)
    return render(request, 'student_dashboard.html', {'group_records': group_records})
