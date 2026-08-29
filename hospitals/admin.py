from django.contrib import admin

from .models import Hospital


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "hospital_type",
        "city",
        "state",
        "phone",
        "emergency_available",
    )

    list_filter = (
        "hospital_type",
        "emergency_available",
        "state",
        "city",
    )

    search_fields = (
        "name",
        "registration_number",
        "city",
        "state",
        "pincode",
    )