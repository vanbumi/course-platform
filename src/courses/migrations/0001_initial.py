# Generated by Django 5.1.2 on 2024-11-01 20:32

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=courses.models.handle_upload)),
                ('access', models.CharField(choices=[('anyone', 'Anyone'), ('email_required', 'Email Required'), ('draft', 'Draft')], default='email_required', max_length=14)),
                ('status', models.CharField(choices=[('published', 'Pub'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='email_required', max_length=14)),
            ],
        ),
    ]
