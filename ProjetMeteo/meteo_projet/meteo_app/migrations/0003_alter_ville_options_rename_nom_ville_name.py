# Generated by Django 4.1.6 on 2023-02-07 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meteo_app', '0002_alter_ville_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ville',
            options={'verbose_name_plural': 'villes'},
        ),
        migrations.RenameField(
            model_name='ville',
            old_name='nom',
            new_name='name',
        ),
    ]