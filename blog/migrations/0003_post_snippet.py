# Generated by Django 3.2 on 2023-02-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click button to read blog post...', max_length=2000),
        ),
    ]
