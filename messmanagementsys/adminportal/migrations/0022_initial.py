# Generated by Django 4.1.7 on 2023-03-01 14:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminportal', '0021_remove_messfee_std_id_delete_messmenu_delete_person_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.TextField(null=True)),
                ('tuesday', models.TextField(null=True)),
                ('wednesday', models.TextField(null=True)),
                ('thursday', models.TextField(null=True)),
                ('friday', models.TextField(null=True)),
                ('saturday', models.TextField(null=True)),
                ('sunday', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('phone_num', models.CharField(max_length=112, validators=[django.core.validators.RegexValidator(message='Enter phone number without +91', regex='^\\+?1?\\d{9,10}$')])),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('hostel', models.CharField(max_length=100, verbose_name='Hostel Name')),
                ('room_no', models.IntegerField(verbose_name='Room No.')),
            ],
        ),
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MessFee',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Transaction ID')),
                ('reciept_id', models.IntegerField(unique=True, verbose_name='Reciept ID')),
                ('paid_amount', models.IntegerField(default=0, verbose_name='Amount Paid')),
                ('bal_amount', models.IntegerField(default=0, verbose_name='Balance')),
                ('Pay_date', models.DateTimeField(auto_now=True, verbose_name='Payment')),
                ('fee_month', models.DateField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminportal.student', verbose_name='Student ID')),
            ],
        ),
    ]
