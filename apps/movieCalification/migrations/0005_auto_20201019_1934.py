# Generated by Django 3.0.7 on 2020-10-20 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieCalification', '0004_auto_20201019_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='año',
            new_name='anio',
        ),
    ]