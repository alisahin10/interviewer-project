# Generated by Django 4.2.7 on 2023-11-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0004_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
