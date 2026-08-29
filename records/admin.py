from django.contrib import admin

from .models import (
    MedicalRecord,
    Prescription
)


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "doctor",
        "diagnosis",
        "record_date",
    )

    list_filter = (
        "diagnosis",
        "record_date",
    )

    search_fields = (
        "patient__username",
        "doctor__username",
        "diagnosis",
    )


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):

    list_display = (
        "medicine_name",
        "dosage",
        "frequency",
        "duration",
    )

    search_fields = (
        "medicine_name",
    )