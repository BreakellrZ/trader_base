# Generated by Django 4.2.13 on 2024-07-18 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0004_rename_user_checkbox_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkbox',
            old_name='title',
            new_name='add_to_list',
        ),
    ]
