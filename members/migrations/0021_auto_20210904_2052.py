# Generated by Django 3.2.7 on 2021-09-04 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0020_alter_member_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name1',
            new_name='fname1',
        ),
        migrations.AddField(
            model_name='member',
            name='lname1',
            field=models.CharField(default='change', max_length=100),
            preserve_default=False,
        ),
    ]
