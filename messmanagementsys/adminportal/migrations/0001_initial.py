# Generated by Django 4.1.7 on 2023-02-24 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=100)),
                ('std_phnum', models.IntegerField(max_length=12, unique=True)),
                ('std_email', models.EmailField(max_length=255, unique=True)),
                ('std_hostel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciept_id', models.IntegerField(max_length=5, unique=True)),
                ('paid_amt', models.IntegerField(max_length=10)),
                ('bal_amt', models.IntegerField(max_length=10)),
                ('std_phnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminportal.students')),
            ],
        ),
    ]