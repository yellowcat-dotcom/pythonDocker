# Generated by Django 3.2.10 on 2024-02-03 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_file_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='files',
        ),
        migrations.AddField(
            model_name='file',
            name='record',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='myapp.record'),
            preserve_default=False,
        ),
    ]
