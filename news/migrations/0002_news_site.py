# Generated by Django 4.0.2 on 2022-07-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="site",
            field=models.CharField(max_length=50),
            preserve_default=False,
        ),
    ]
