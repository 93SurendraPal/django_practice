# Generated by Django 4.2.18 on 2025-02-05 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
        migrations.AlterModelTable(
            name='classname',
            table='classname',
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
    ]
