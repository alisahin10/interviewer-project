# Generated by Django 4.2.7 on 2023-11-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0008_question_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('test_name', models.CharField(max_length=200)),
                ('department_name', models.CharField(max_length=200)),
                ('number_of_questions', models.CharField(max_length=200)),
                ('question_number', models.CharField(max_length=200)),
                ('correct_answer', models.CharField(max_length=200)),
                ('question_image', models.ImageField(upload_to='test/')),
            ],
        ),
    ]
