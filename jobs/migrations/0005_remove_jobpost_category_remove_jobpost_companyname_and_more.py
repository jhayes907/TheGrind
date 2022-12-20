# Generated by Django 4.1.4 on 2022-12-19 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_company_options_remove_company_listings_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='companyName',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='category',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='companyName',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
