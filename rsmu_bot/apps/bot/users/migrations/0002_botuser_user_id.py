# Generated by Django 5.0.6 on 2024-07-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='user_id',
            field=models.PositiveIntegerField(blank=True, default=11111, unique=True),
            preserve_default=False,
        ),
    ]
