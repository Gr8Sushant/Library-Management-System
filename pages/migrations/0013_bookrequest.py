# Generated by Django 3.2 on 2021-05-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_categories_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('book_name', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
            ],
        ),
    ]
