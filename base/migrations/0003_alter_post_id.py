# Generated by Django 5.2 on 2025-04-14 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
