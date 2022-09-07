# Generated by Django 4.1.1 on 2022-09-07 16:51

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("school_name", models.CharField(max_length=200)),
                ("school_address", models.CharField(max_length=200)),
                ("established_date", models.CharField(max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=200
                    ),
                ),
                ("student_name", models.CharField(max_length=200)),
                ("student_fathers_name", models.CharField(max_length=200)),
                ("student_address", models.CharField(max_length=200)),
                ("academic_year", models.CharField(max_length=200)),
                ("program", models.CharField(max_length=200)),
                ("passed_year", models.CharField(max_length=200)),
                ("secured_gpa", models.CharField(max_length=200)),
                ("date_of_birth", models.DateField()),
                ("symbol_number", models.CharField(max_length=200)),
                ("registration_number", models.CharField(max_length=200)),
                ("issued_date", models.CharField(max_length=200)),
                (
                    "certificate",
                    versatileimagefield.fields.VersatileImageField(
                        null=True, upload_to="media/"
                    ),
                ),
            ],
        ),
    ]
