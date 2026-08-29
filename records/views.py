from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from accounts.models import DoctorProfile, CitizenProfile

from .models import MedicalRecord
from .forms import (
    MedicalRecordForm,
    PrescriptionForm
)


@login_required
def create_medical_record(
    request,
    patient_id,
    appointment_id=None
):

    doctor_profile = get_object_or_404(
        DoctorProfile,
        user=request.user
    )

    if request.method == "POST":

        form = MedicalRecordForm(
            request.POST
        )

        if form.is_valid():

            record = form.save(
                commit=False
            )

            record.patient_id = patient_id
            record.doctor = request.user

            if appointment_id:
                record.appointment_id = appointment_id

            record.save()

            messages.success(
                request,
                "Medical record created."
            )

            return redirect(
                "records:doctor_patient_records",
                patient_id=patient_id
            )

    else:

        form = MedicalRecordForm()

    return render(
        request,
        "records/create_record.html",
        {
            "form": form,
            "patient_id": patient_id,
            "appointment_id": appointment_id,
        }
    )


@login_required
def doctor_patient_records(
    request,
    patient_id
):

    records = MedicalRecord.objects.filter(
        patient_id=patient_id
    ).select_related(
        "doctor"
    ).prefetch_related(
        "prescriptions"
    )

    patient = get_object_or_404(
        CitizenProfile.objects.select_related("user"),
        user_id=patient_id
    )

    return render(
        request,
        "records/doctor_patient_records.html",
        {
            "records": records,
            "patient_id": patient_id,
            "patient": patient
        }
    )


@login_required
def search_patient_records(request):

    citizen = None
    error = None

    if request.method == "POST":

        onehealth_id = request.POST.get(
            "onehealth_id",
            ""
        ).strip().upper()

        if onehealth_id:

            try:

                citizen = CitizenProfile.objects.select_related(
                    "user"
                ).get(
                    onehealth_id=onehealth_id
                )

                return redirect(
                    "records:doctor_patient_records",
                    patient_id=citizen.user.id
                )

            except CitizenProfile.DoesNotExist:

                error = (
                    "No citizen found with this OneHealth ID."
                )

        else:

            error = "Please enter a OneHealth ID."

    return render(
        request,
        "records/search_patient.html",
        {
            "error": error,
            "citizen": citizen
        }
    )


@login_required
def citizen_records(request):

    records = MedicalRecord.objects.filter(
        patient=request.user
    ).select_related(
        "doctor",
        "appointment"
    ).prefetch_related(
        "prescriptions"
    )

    return render(
        request,
        "records/citizen_records.html",
        {
            "records": records
        }
    )


@login_required
def add_prescription(
    request,
    record_id
):

    record = get_object_or_404(
        MedicalRecord,
        id=record_id,
        doctor=request.user
    )

    if request.method == "POST":

        form = PrescriptionForm(
            request.POST
        )

        if form.is_valid():

            prescription = form.save(
                commit=False
            )

            prescription.medical_record = record

            prescription.save()

            messages.success(
                request,
                "Prescription added."
            )

            return redirect(
                "records:doctor_patient_records",
                patient_id=record.patient.id
            )

    else:

        form = PrescriptionForm()

    return render(
        request,
        "records/add_prescription.html",
        {
            "form": form,
            "record": record
        }
    )