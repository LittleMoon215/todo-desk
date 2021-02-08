# Generated by Django 3.1.5 on 2021-02-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20210201_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(default='08.02.2021 09:45'),
        ),
    ]