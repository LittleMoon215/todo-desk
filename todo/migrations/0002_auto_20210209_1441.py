# Generated by Django 3.1.5 on 2021-02-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(default='09.02.2021 07:41'),
        ),
    ]
