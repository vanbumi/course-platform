# Generated by Django 5.1.2 on 2024-11-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='access',
            field=models.CharField(choices=[('anyone', 'Anyone'), ('email', 'Email Required'), ('draft', 'Draft')], default='email', max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('published', 'Pub'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='email', max_length=14),
        ),
    ]