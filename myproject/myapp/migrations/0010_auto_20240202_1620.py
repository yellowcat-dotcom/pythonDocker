# Generated by Django 3.2.10 on 2024-02-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_file_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachergroup',
            name='group',
        ),
        migrations.RemoveField(
            model_name='teachergroup',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='discipline',
            name='group',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='groups',
        ),
        migrations.AddField(
            model_name='discipline',
            name='groups',
            field=models.ManyToManyField(to='myapp.Group'),
        ),
        migrations.AlterField(
            model_name='group',
            name='number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.RemoveField(
            model_name='record',
            name='files',
        ),
        migrations.AddField(
            model_name='record',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='TeacherGroup',
        ),
    ]
