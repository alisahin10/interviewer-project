# Generated by Django 4.2.7 on 2023-11-28 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0015_question_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='number_of_questions',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
