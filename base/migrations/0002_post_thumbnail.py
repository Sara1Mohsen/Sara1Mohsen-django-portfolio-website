# Generated by Django 5.2 on 2025-04-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images/'),
        ),
    ]
