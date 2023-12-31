# Generated by Django 4.1 on 2022-11-12 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("name", models.CharField(max_length=50)),
                ("d_dob", models.DateField()),
                ("d_email", models.CharField(max_length=100)),
                ("mobile", models.IntegerField()),
                ("d_aadhar", models.IntegerField()),
                ("specialization", models.CharField(max_length=50)),
                ("qualification", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
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
                ("registrationDate", models.DateField()),
                ("name", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=10)),
                ("p_dob", models.DateField()),
                ("mobile", models.IntegerField(null=True)),
                ("p_email", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=150)),
                ("p_aadhar", models.IntegerField(max_length=12)),
                ("state", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("bloodgroup", models.CharField(max_length=3)),
                ("disease", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
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
                ("date1", models.DateField(null=True)),
                ("time1", models.TimeField(max_length=150)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.doctor",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.patient",
                    ),
                ),
            ],
        ),
    ]
