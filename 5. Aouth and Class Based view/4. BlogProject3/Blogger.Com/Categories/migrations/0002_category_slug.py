# Generated by Django 4.2.7 on 2023-12-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
