# Generated by Django 4.2.7 on 2024-01-21 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0015_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
