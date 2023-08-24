# Generated by Django 4.1 on 2022-11-15 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0004_alter_patient_mobile_alter_patient_p_aadhar"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prescription",
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
                ("med", models.CharField(max_length=150)),
                ("dnd", models.CharField(max_length=150)),
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
