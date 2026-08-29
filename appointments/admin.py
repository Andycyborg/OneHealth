from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "citizen",
        "doctor",
        "hospital",
        "appointment_date",
        "appointment_time",
        "status",
    )

    list_filter = (
        "status",
        "appointment_date",
        "hospital",
    )

    search_fields = (
        "citizen__username",
        "doctor__username",
        "hospital__name",
    )