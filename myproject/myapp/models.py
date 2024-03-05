from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, unique=True)
    father_name = models.CharField(max_length=50)
    disciplines = models.ManyToManyField('Discipline', through='DisciplineTeacher', blank=True)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.father_name}'


class Group(models.Model):
    number = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False}, unique=True)

    def __str__(self):
        return str(self.number)


class Discipline(models.Model):
    name = models.CharField(max_length=100, unique=True)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.name


class DisciplineTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher} - {self.discipline}'


class Record(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='records')
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    group = models.ManyToManyField(Group)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def formatted_date(self):
        return timezone.localtime(self.date).strftime('%d.%m.%Y %H:%M')

    def __str__(self):
        return f'{self.discipline} - {self.group} - {self.formatted_date()}'


class File(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return str(self.file)
