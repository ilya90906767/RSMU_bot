# Generated by Django 5.0.6 on 2024-07-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_botuser_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='user_id',
            field=models.PositiveBigIntegerField(blank=True, unique=True),
        ),
    ]
