# Generated by Django 3.2.7 on 2021-09-04 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_alter_member_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='note',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
