# Generated by Django 3.1.5 on 2021-02-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20210209_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(default='09.02.2021 08:37'),
        ),
    ]