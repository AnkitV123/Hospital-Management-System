# Generated by Django 4.1 on 2022-11-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="p_aadhar",
            field=models.IntegerField(),
        ),
    ]
