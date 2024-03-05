from django.contrib import admin
from .models import Teacher, Group, Discipline, DisciplineTeacher, Record, File


class FileInline(admin.StackedInline):  # (admin.StackedInline)
    model = File


class RecordAdmin(admin.ModelAdmin):
    inlines = [FileInline]
    fields = ('discipline', 'group', 'description')
    list_display = ('discipline', 'formatted_date', 'teacher', 'get_group', 'description')
    search_fields = ['discipline__name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return qs
            elif hasattr(request.user, 'teacher'):
                return qs.filter(teacher=request.user.teacher)
        return qs.none()

    def save_model(self, request, obj, form, change):
        if not change and request.user.is_authenticated and hasattr(request.user, 'teacher'):
            obj.teacher = request.user.teacher
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'teacher' and request.user.is_authenticated and hasattr(request.user, 'teacher'):
            kwargs['queryset'] = Teacher.objects.filter(id=request.user.teacher.id)
            kwargs['initial'] = request.user.teacher.id
        elif db_field.name == 'discipline' and request.user.is_authenticated and hasattr(request.user, 'teacher'):
            kwargs['queryset'] = Discipline.objects.filter(disciplineteacher__teacher=request.user.teacher)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_group(self, obj):
        return ', '.join([str(group) for group in obj.group.all()])

    get_group.short_description = 'Group'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('number',)
    # добавить фильтрацию по номеру группы


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ['user__first_name', 'user__last_name']

    def full_name(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name} {obj.father_name}'


@admin.register(DisciplineTeacher)
class DisciplineTeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'discipline')
    list_filter = ('teacher',)
    search_fields = ['teacher__user__first_name', 'teacher__user__last_name', 'discipline__name']


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'group_display')
    search_fields = ['name']

    def group_display(self, obj):
        return ', '.join([str(group) for group in obj.groups.all()])

    group_display.short_description = 'Groups'  # Устанавливаем короткое описание для колонки


class FileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'views_count')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Проверка, является ли пользователь администратором
            return qs
        elif hasattr(request.user, 'teacher'):  # Проверка, является ли пользователь преподавателем
            return qs.filter(record__teacher=request.user.teacher)
        else:
            return qs.none()


admin.site.register(File, FileAdmin)

admin.site.register(Record, RecordAdmin)
# admin.site.register(File)

admin.site.site_header = 'Привет преподаватель!'
