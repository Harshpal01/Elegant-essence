# salon/models.py

from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)  # Assuming you have icons for services

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    required_services = models.ManyToManyField(Service)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line

    def __str__(self):
        return f"Booking by {self.name} on {self.created_at}"
