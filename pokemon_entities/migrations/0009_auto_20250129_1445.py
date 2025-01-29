# Generated by Django 3.1.14 on 2025-01-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_pokemon_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title',
            new_name='title_ru',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(default='Нет доступного описания', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(default='Нет доступного описания', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
