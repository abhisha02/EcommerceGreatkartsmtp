# Generated by Django 4.2.9 on 2024-01-22 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_category_cat_is_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_is_available',
            new_name='is_available',
        ),
    ]
