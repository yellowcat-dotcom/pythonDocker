from django.urls import path
from .views import student_dashboard, login_view

urlpatterns = [
    # Маршрут для страницы входа студентов
    path('login/', login_view, name='student_login'),
    path('dashboard/', student_dashboard, name='student_dashboard'),

]