# Generated by Django 4.2.7 on 2023-12-12 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_alter_posts_author'),
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
