# Generated by Django 4.2.7 on 2023-11-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0016_alter_question_number_of_questions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_home',
            field=models.BooleanField(default=True),
        ),
    ]
