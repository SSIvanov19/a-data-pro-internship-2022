# Generated by Django 4.0.2 on 2022-07-04 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_news_site"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"managed": True},
        ),
        migrations.AlterModelOptions(
            name="newsimage",
            options={"managed": True},
        ),
        migrations.AlterField(
            model_name="news",
            name="pub_date",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(max_length=180),
        ),
        migrations.AlterField(
            model_name="news",
            name="url",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
