# Generated by Django 3.2.7 on 2021-09-04 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20210904_0221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='address',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='member',
            name='address2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='member',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='state',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='member',
            name='zip',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='email1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='email2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership_status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership_type',
            field=models.CharField(blank=True, choices=[('supporter', 'supporter'), ('volunteer', 'volunteer'), ('comp', 'comp'), ('board', 'board')], default='supporter', max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
