# Generated by Django 4.1 on 2022-11-17 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='salesman',
            new_name='warehouse',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='salesman',
            new_name='warehouse',
        ),
        migrations.RenameField(
            model_name='statistics',
            old_name='salesman',
            new_name='warehouse',
        ),
    ]
