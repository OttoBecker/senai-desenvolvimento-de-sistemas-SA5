# Generated by Django 5.0.3 on 2024-04-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_aula', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nascimento',
            field=models.IntegerField(),
        ),
    ]
