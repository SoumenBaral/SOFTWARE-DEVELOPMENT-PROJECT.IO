# Generated by Django 4.2.7 on 2023-12-16 11:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.ratings'),
        ),
        migrations.AlterField(
            model_name='album',
            name='releaseDate',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
