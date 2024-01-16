from django.contrib import admin
from .models import Record, Teacher, Discipline, Group, File, DisciplineTeacher


class RecordAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'formatted_date', 'group', 'teachers_display')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif hasattr(request.user, 'teacher'):
            # Если пользователь - преподаватель, фильтруем записи по преподавателю
            return qs.filter(teachers=request.user.teacher)
        else:
            # Если пользователь не администратор и не преподаватель, не показываем ничего
            return qs.none()

    def teachers_display(self, obj):
        return ", ".join([str(teacher) for teacher in obj.teachers.all()])

    teachers_display.short_description = 'Teachers'


admin.site.register(Record, RecordAdmin)
admin.site.register(Teacher)
admin.site.register(Discipline)
admin.site.register(Group)
admin.site.register(File)
