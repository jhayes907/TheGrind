# Generated by Django 4.1.4 on 2022-12-19 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_alter_jobpost_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='salary',
        ),
    ]
