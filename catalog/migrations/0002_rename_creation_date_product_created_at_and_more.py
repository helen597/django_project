# Generated by Django 5.0.2 on 2024-02-18 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='creation_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='edit_date',
            new_name='updated_at',
        ),
    ]
