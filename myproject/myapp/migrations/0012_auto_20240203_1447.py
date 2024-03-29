# Generated by Django 3.2.10 on 2024-02-03 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_group_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='files',
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='files',
            field=models.ManyToManyField(to='myapp.File'),
        ),
    ]
