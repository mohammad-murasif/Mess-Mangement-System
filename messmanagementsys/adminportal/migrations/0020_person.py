# Generated by Django 4.1.7 on 2023-02-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0019_student_messfee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marks', models.CharField(max_length=100)),
            ],
        ),
    ]
