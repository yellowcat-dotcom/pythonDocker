# Generated by Django 3.2.10 on 2024-01-16 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_record_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='description',
        ),
    ]
