# Generated by Django 3.2 on 2023-02-01 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='product_size',
            new_name='product_color',
        ),
    ]
