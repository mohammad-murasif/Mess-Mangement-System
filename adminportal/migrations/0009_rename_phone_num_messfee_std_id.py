# Generated by Django 4.1.7 on 2023-02-25 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0008_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messfee',
            old_name='phone_num',
            new_name='std_id',
        ),
    ]