# Generated by Django 4.2.11 on 2024-04-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="pic",
            field=models.ImageField(default="no_picture.jpg", upload_to="books"),
        ),
    ]
