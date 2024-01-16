from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.surname} {self.name} {self.father_name}'


class Group(models.Model):
    number = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DisciplineTeacher(models.Model):
    record = models.ForeignKey('Record', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Record(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    file = models.ManyToManyField('File')  # Предполагается, что у вас есть модель File для хранения файлов
    date = models.DateTimeField(auto_now_add=True)
    teachers = models.ManyToManyField(Teacher, through=DisciplineTeacher, blank=True, related_name='disciplines')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def formatted_date(self):
        return self.date.strftime('%d.%m.%Y %H:%M')

    def __str__(self):
        return f'{self.discipline} - {self.group} - {self.formatted_date()}'


class File(models.Model):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return str(self.file)
