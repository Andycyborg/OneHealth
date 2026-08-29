from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from accounts.models import DoctorProfile
from hospitals.models import Hospital

from .models import Appointment
from .forms import AppointmentForm


@login_required
def book_appointment(
    request,
    hospital_id,
    doctor_id
):

    hospital = get_object_or_404(
        Hospital,
        id=hospital_id
    )

    doctor_profile = get_object_or_404(
        DoctorProfile,
        id=doctor_id
    )

    doctor = doctor_profile.user

    # Make sure doctor actually works
    # at this hospital.
    if not doctor_profile.hospitals.filter(
        id=hospital.id
    ).exists():

        messages.error(
            request,
            "This doctor is not associated with this hospital."
        )

        return redirect(
            "hospitals:hospital_detail",
            hospital_id=hospital.id
        )

    if request.method == "POST":

        form = AppointmentForm(
            request.POST
        )

        if form.is_valid():

            appointment = form.save(
                commit=False
            )

            appointment.citizen = request.user
            appointment.doctor = doctor
            appointment.hospital = hospital

            try:

                appointment.save()

            except IntegrityError:

                form.add_error(
                    None,
                    "This doctor already has an appointment "
                    "at this date and time. Please choose "
                    "another time."
                )

            else:

                messages.success(
                    request,
                    "Appointment booked successfully."
                )

                return redirect(
                    "appointments:citizen_appointments"
                )

    else:

        form = AppointmentForm()

    return render(
        request,
        "appointments/book_appointment.html",
        {
            "form": form,
            "hospital": hospital,
            "doctor": doctor_profile,
        }
    )


@login_required
def citizen_appointments(request):

    appointments = (
        Appointment.objects
        .filter(
            citizen=request.user
        )
        .select_related(
            "doctor",
            "doctor__doctor_profile",
            "hospital"
        )
    )

    return render(
        request,
        "appointments/citizen_appointments.html",
        {
            "appointments": appointments
        }
    )


@login_required
def doctor_appointments(request):

    doctor_profile = get_object_or_404(
        DoctorProfile,
        user=request.user
    )

    appointments = (
        Appointment.objects
        .filter(
            doctor=request.user
        )
        .select_related(
            "citizen",
            "hospital"
        )
    )

    return render(
        request,
        "appointments/doctor_appointments.html",
        {
            "appointments": appointments,
            "doctor": doctor_profile,
        }
    )


@login_required
def update_appointment(
    request,
    appointment_id
):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor=request.user
    )

    if request.method == "POST":

        status = request.POST.get(
            "status"
        )

        allowed_statuses = [
            "Accepted",
            "Rejected",
            "Completed",
        ]

        if status in allowed_statuses:

            appointment.status = status

            appointment.doctor_note = (
                request.POST.get(
                    "doctor_note",
                    ""
                ).strip()
            )

            appointment.save()

            messages.success(
                request,
                "Appointment updated successfully."
            )

    return redirect(
        "appointments:doctor_appointments"
    )


@login_required
def cancel_appointment(
    request,
    appointment_id
):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        citizen=request.user
    )

    if appointment.status == "Pending":

        appointment.status = "Cancelled"

        appointment.save()

        messages.success(
            request,
            "Appointment cancelled successfully."
        )

    else:

        messages.error(
            request,
            "Only pending appointments can be cancelled."
        )

    return redirect(
        "appointments:citizen_appointments"
    )


@login_required
def appointment_list(request):

    if hasattr(
        request.user,
        "doctor_profile"
    ):

        return redirect(
            "appointments:doctor_appointments"
        )

    return redirect(
        "appointments:citizen_appointments"
    )