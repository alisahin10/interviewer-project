# Generated by Django 4.2.7 on 2023-12-01 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0020_testdetail_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testdetail',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='test_detail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='interviewer.testdetail'),
        ),
    ]
