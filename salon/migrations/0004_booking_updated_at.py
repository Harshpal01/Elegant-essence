# Generated by Django 5.0.7 on 2024-07-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salon", "0003_rename_date_booked_booking_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
