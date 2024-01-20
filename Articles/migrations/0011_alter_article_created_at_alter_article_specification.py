# Generated by Django 4.2.7 on 2024-01-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0010_alter_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='specification',
            field=models.CharField(max_length=50),
        ),
    ]