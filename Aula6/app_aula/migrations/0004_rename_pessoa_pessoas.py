# Generated by Django 5.0.3 on 2024-04-14 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_aula', '0002_alter_pessoa_idade'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pessoa',
            new_name='Pessoas',
        ),
    ]
