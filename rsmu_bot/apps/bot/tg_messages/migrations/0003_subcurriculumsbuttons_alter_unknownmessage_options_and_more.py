# Generated by Django 4.2.13 on 2024-07-09 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tg_messages', '0002_remove_curriculumsmessage_image_curriculumsbuttons'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCurriculumsButtons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('message', models.TextField(max_length=4000)),
                ('image', models.ImageField(blank=True, upload_to='subcurriculumsbuttons_img')),
                ('link', models.CharField(max_length=400)),
                ('state', models.CharField(choices=[('A', 'Активно'), ('N', 'Неактивно')], max_length=1)),
                ('curriculums_buttons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tg_messages.curriculumsbuttons')),
            ],
            options={
                'verbose_name': 'Направления внеучебной деятельности',
            },
        ),
        migrations.AlterModelOptions(
            name='unknownmessage',
            options={'verbose_name': 'Подразделения'},
        ),
        migrations.CreateModel(
            name='SubSubCurriculumsButtons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('message', models.TextField(max_length=4000)),
                ('image', models.ImageField(blank=True, upload_to='subsubcurriculumsbuttons_img')),
                ('link', models.CharField(max_length=400)),
                ('state', models.CharField(choices=[('A', 'Активно'), ('N', 'Неактивно')], max_length=1)),
                ('subcurriculums_buttons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tg_messages.subcurriculumsbuttons')),
            ],
            options={
                'verbose_name': 'Секции у Направления',
            },
        ),
    ]
