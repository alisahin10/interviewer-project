# Generated by Django 4.2.7 on 2023-11-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0011_question_correct_answer_question_department_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='dropdown',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
