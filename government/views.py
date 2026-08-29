from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import (
    CitizenProfile,
    DoctorProfile,
    GovernmentProfile
)

from hospitals.models import Hospital
from records.models import MedicalRecord
from appointments.models import Appointment


@login_required
def dashboard(request):

    government_profile = request.user.government_profile

    records = MedicalRecord.objects.all()

    disease_data = (
        records
        .values("diagnosis")
        .annotate(
            total=__import__(
                "django.db.models",
                fromlist=["Count"]
            ).Count("id")
        )
        .order_by("-total")
    )

    area_data = (
        CitizenProfile.objects
        .exclude(address="")
        .values("address")
        .annotate(
            total=__import__(
                "django.db.models",
                fromlist=["Count"]
            ).Count("id")
        )
        .order_by("-total")[:10]
    )

    context = {

        "profile": government_profile,

        "citizen_count":
            CitizenProfile.objects.count(),

        "doctor_count":
            DoctorProfile.objects.count(),

        "hospital_count":
            Hospital.objects.count(),

        "appointment_count":
            Appointment.objects.count(),

        "record_count":
            records.count(),

        "disease_data":
            disease_data,

        "area_data":
            area_data,

    }

    return render(
        request,
        "government/dashboard.html",
        context
    )