# Generated by Django 3.1.14 on 2025-01-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20250125_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.CharField(default='Нет доступного описания', max_length=200),
            preserve_default=False,
        ),
    ]
