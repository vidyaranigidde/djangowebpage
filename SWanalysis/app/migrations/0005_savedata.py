# Generated by Django 2.2.9 on 2020-01-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191229_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.TextField(null=True)),
                ('resident', models.TextField(null=True)),
                ('rperiod', models.TextField(null=True)),
                ('operiod', models.TextField(null=True)),
                ('diam', models.TextField(null=True)),
                ('cli', models.TextField(null=True)),
                ('grav', models.TextField(null=True)),
            ],
        ),
    ]