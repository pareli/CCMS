# Generated by Django 4.1.1 on 2022-09-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="registration_number",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
