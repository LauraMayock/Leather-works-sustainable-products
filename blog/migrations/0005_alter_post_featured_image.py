# Generated by Django 3.2 on 2023-02-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]