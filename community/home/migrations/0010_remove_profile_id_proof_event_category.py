# Generated by Django 4.2.4 on 2023-10-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_profile_id_proof"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="id_proof",
        ),
        migrations.AddField(
            model_name="event",
            name="category",
            field=models.CharField(default="Other", max_length=25),
        ),
    ]
