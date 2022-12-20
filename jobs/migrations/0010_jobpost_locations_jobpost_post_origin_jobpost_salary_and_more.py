# Generated by Django 4.1.4 on 2022-12-19 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_remove_jobpost_locations_remove_jobpost_post_origin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='locations',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='post_origin',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='salary',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='stack',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='locations',
            field=models.TextField(default=None, null=True),
        ),
    ]
