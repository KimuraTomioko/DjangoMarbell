# Generated by Django 5.0.13 on 2025-03-28 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marbell', '0006_house_spain_housephoto_spain'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house_spain',
            options={'verbose_name': 'Дом исп.', 'verbose_name_plural': 'Дома исп.'},
        ),
        migrations.AlterModelOptions(
            name='housephoto_spain',
            options={'verbose_name': 'Фотография дома исп.', 'verbose_name_plural': 'Фотографии домов исп.'},
        ),
    ]
