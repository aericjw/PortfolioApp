# Generated by Django 4.1 on 2022-08-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Portfolio", "0004_about"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
