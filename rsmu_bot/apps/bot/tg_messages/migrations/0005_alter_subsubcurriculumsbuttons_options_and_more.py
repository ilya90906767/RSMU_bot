# Generated by Django 4.2.13 on 2024-07-10 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tg_messages', '0004_alter_subcurriculumsbuttons_link_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subsubcurriculumsbuttons',
            options={'verbose_name': 'Подразделения у Направления'},
        ),
        migrations.AlterModelOptions(
            name='unknownmessage',
            options={'verbose_name': 'Текст при Неизвестном сообщении'},
        ),
    ]
