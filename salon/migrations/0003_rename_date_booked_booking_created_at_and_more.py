# Generated by Django 5.0.7 on 2024-07-25 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salon", "0002_booking_service_icon_alter_service_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="date_booked",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="phone",
            new_name="phone_number",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="services",
        ),
        migrations.AddField(
            model_name="booking",
            name="required_services",
            field=models.ManyToManyField(to="salon.service"),
        ),
        migrations.AlterField(
            model_name="service",
            name="icon",
            field=models.ImageField(blank=True, null=True, upload_to="icons/"),
        ),
    ]
