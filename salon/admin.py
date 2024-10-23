# salon/admin.py

from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('created_at', 'updated_at')


