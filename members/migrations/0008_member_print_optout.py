# Generated by Django 3.2.7 on 2021-09-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20210904_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='print_optout',
            field=models.BooleanField(default=False),
        ),
    ]
