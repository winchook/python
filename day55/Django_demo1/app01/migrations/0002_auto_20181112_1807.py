# Generated by Django 2.1.3 on 2018-11-12 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classes',
            old_name='titile',
            new_name='title',
        ),
    ]
