from django.urls import path
from .views import student_dashboard, login_view, logout_view, group_records

urlpatterns = [
    # Маршрут для страницы входа студентов
    path('login/', login_view, name='student_login'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path('logout/', logout_view, name='student_logout'),
    path('group/<int:group_id>/records/', group_records, name='student_dashboard'),
]