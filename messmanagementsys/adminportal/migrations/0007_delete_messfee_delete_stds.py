# Generated by Django 4.1.7 on 2023-02-25 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0006_messfee_stds_delete_amount_delete_students_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MessFee',
        ),
        migrations.DeleteModel(
            name='Stds',
        ),
    ]
