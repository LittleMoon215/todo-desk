# Generated by Django 3.1.5 on 2021-01-28 05:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210124_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(default='28.01.2021 05:45'),
        ),
    ]
