# Generated by Django 3.1.7 on 2022-02-24 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Data',
            new_name='ToDo',
        ),
    ]