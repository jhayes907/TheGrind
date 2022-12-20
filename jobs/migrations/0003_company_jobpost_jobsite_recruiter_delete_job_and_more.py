# Generated by Django 4.1.4 on 2022-12-19 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0002_alter_job_options_remove_job_name_job_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('locations', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=50, unique=True)),
                ('response', models.TextField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('companyName', models.CharField(max_length=40)),
                ('title', models.TextField(default=None, max_length=30)),
                ('locations', models.CharField(max_length=20)),
                ('salary', models.IntegerField(blank=True)),
                ('stack', models.CharField(max_length=150)),
                ('content', models.URLField(default=None)),
                ('response', models.TextField(blank=True, null=True)),
                ('post_origin', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='JobSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('listings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobpost')),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('response', models.TextField(blank=True, null=True)),
                ('listings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobpost')),
            ],
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.AddField(
            model_name='company',
            name='listings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobpost'),
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
