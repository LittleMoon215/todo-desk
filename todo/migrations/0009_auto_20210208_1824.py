# Generated by Django 3.1.5 on 2021-02-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20210208_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(default='08.02.2021 11:23'),
        ),
    ]
