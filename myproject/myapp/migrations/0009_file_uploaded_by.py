# Generated by Django 3.2.10 on 2024-01-16 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20240116_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.teacher'),
            preserve_default=False,
        ),
    ]