# Generated by Django 3.1.2 on 2021-03-14 21:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_auto_20210314_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='participants',
            field=models.TextField(default=[]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='podcast',
            name='uploaded_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
