# Generated by Django 3.2.7 on 2021-09-04 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_rename_print_optout_member_directory_optout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='zip',
            new_name='postal',
        ),
    ]