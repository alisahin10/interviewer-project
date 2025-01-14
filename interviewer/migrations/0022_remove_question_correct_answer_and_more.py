# Generated by Django 4.2.7 on 2023-12-01 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0021_remove_testdetail_question_question_test_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='number_of_questions',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_description',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_number',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_title',
        ),
        migrations.RemoveField(
            model_name='question',
            name='test_detail',
        ),
        migrations.RemoveField(
            model_name='question',
            name='test_name',
        ),
        migrations.AddField(
            model_name='testdetail',
            name='test_detail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='interviewer.question'),
        ),
    ]
