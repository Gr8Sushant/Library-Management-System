# Generated by Django 3.2 on 2021-05-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='text',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
