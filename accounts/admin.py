from django.contrib import admin

from .models import (
    CitizenProfile,
    DoctorProfile,
    GovernmentProfile
)


@admin.register(CitizenProfile)
class CitizenProfileAdmin(admin.ModelAdmin):

    list_display = (
        "onehealth_id",
        "user",
        "gender",
        "blood_group",
        "phone",
        "created_at",
    )

    search_fields = (
        "onehealth_id",
        "user__username",
        "user__first_name",
        "user__last_name",
    )


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):

    list_display = (
        "doctor_id",
        "user",
        "specialization",
        "experience",
    )

    list_filter = (
        "specialization",
    )

    search_fields = (
        "doctor_id",
        "user__username",
        "user__first_name",
        "user__last_name",
        "specialization",
    )

    filter_horizontal = (
        "hospitals",
    )


@admin.register(GovernmentProfile)
class GovernmentProfileAdmin(admin.ModelAdmin):

    list_display = (
        "officer_id",
        "user",
        "department",
        "area",
        "phone",
    )

    search_fields = (
        "officer_id",
        "user__username",
        "user__first_name",
        "user__last_name",
        "department",
        "area",
    )