# Generated by Django 4.2.13 on 2024-07-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_checkbox_description_checkbox_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkbox',
            name='description',
        ),
        migrations.AddField(
            model_name='checkbox',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
