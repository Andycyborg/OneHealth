from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Count
from appointments.models import Appointment

from .forms import (
    CitizenRegistrationForm,
    DoctorRegistrationForm,
    GovernmentRegistrationForm
)


def home(request):
    return render(request, "home.html")


def register(request):

    role = request.POST.get("role", "citizen")

    form = CitizenRegistrationForm()

    if request.method == "POST":

        if role == "citizen":

            form = CitizenRegistrationForm(request.POST)

        elif role == "doctor":

            form = DoctorRegistrationForm(request.POST)

        elif role == "government":

            form = GovernmentRegistrationForm(request.POST)

        else:

            form = CitizenRegistrationForm()

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect(
                "accounts:dashboard_redirect"
            )

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
            "selected_role": role
        }
    )


def login_view(request):

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect(
                "accounts:dashboard_redirect"
            )

        error = "Invalid username or password."

    return render(
        request,
        "accounts/login.html",
        {
            "error": error
        }
    )


@login_required
def dashboard_redirect(request):

    user = request.user

    if hasattr(user, "citizen_profile"):
        return redirect("accounts:citizen_dashboard")

    if hasattr(user, "doctor_profile"):
        return redirect("accounts:doctor_dashboard")

    if hasattr(user, "government_profile"):
        return redirect("government:dashboard")

    return render(
        request,
        "accounts/dashboard_redirect.html"
    )


@login_required
def logout_view(request):

    logout(request)

    return redirect("home")


@login_required
def citizen_dashboard(request):

    from appointments.models import Appointment
    from records.models import MedicalRecord

    profile = request.user.citizen_profile

    appointments = Appointment.objects.filter(
        citizen=request.user
    ).select_related(
        "doctor",
        "hospital"
    )

    records = MedicalRecord.objects.filter(
        patient=request.user
    ).select_related(
        "doctor"
    ).prefetch_related(
        "prescriptions"
    )

    upcoming = appointments.filter(
        status__in=[
            "Pending",
            "Accepted"
        ]
    ).order_by(
        "appointment_date",
        "appointment_time"
    )[:3]

    recent_records = records[:5]

    context = {

        "profile": profile,

        "appointments": appointments,

        "upcoming": upcoming,

        "recent_records": recent_records,

        "appointment_count":
            appointments.count(),

        "record_count":
            records.count(),

    }

    return render(
        request,
        "accounts/citizen_dashboard.html",
        context
    )


@login_required
def doctor_dashboard(request):

    doctor = request.user.doctor_profile

    hospitals = doctor.hospitals.all()

    appointments = (
        Appointment.objects
        .filter(
            doctor=request.user
        )
        .select_related(
            "citizen",
            "hospital"
        )
        .order_by(
            "appointment_date",
            "appointment_time"
        )
    )

    appointments_count = appointments.count()

    pending_count = appointments.filter(
        status="Pending"
    ).count()

    accepted_count = appointments.filter(
        status="Accepted"
    ).count()

    completed_count = appointments.filter(
        status="Completed"
    ).count()

    return render(
        request,
        "accounts/doctor_dashboard.html",
        {
            "profile": doctor,
            "hospitals": hospitals,
            "appointments": appointments,
            "appointments_count": appointments_count,
            "pending_count": pending_count,
            "accepted_count": accepted_count,
            "completed_count": completed_count,
        }
    )