# Generated by Django 4.1.7 on 2023-02-25 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0013_alter_messfee_trans_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='messmenu',
            name='friday',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='saturday',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='sunday',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='thursday',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='tuesday',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='wednesday',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='messfee',
            name='std_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminportal.student', verbose_name='Student ID'),
        ),
        migrations.AlterField(
            model_name='messmenu',
            name='monday',
            field=models.TextField(null=True),
        ),
    ]
