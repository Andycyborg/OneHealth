from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import (
    render,
    get_object_or_404
)

from .models import Hospital


@login_required
def hospital_list(request):

    search = request.GET.get(
        "search",
        ""
    ).strip()

    hospital_type = request.GET.get(
        "type",
        ""
    )

    city = request.GET.get(
        "city",
        ""
    ).strip()

    hospitals = Hospital.objects.all()

    if search:

        hospitals = hospitals.filter(
            Q(name__icontains=search)
            |
            Q(city__icontains=search)
            |
            Q(state__icontains=search)
            |
            Q(pincode__icontains=search)
        )

    if hospital_type:

        hospitals = hospitals.filter(
            hospital_type=hospital_type
        )

    if city:

        hospitals = hospitals.filter(
            city__icontains=city
        )

    hospitals = hospitals.order_by(
        "name"
    )

    return render(
        request,
        "hospitals/hospital_list.html",
        {
            "hospitals": hospitals,
            "search": search,
            "hospital_type": hospital_type,
            "city": city,
        }
    )


@login_required
def hospital_detail(
    request,
    hospital_id
):

    hospital = get_object_or_404(
        Hospital,
        id=hospital_id
    )

    specialization = request.GET.get(
        "specialization",
        ""
    ).strip()

    doctors = (
        hospital.doctors
        .select_related("user")
        .all()
    )

    if specialization:

        doctors = doctors.filter(
            specialization__icontains=specialization
        )

    doctors = doctors.order_by(
        "specialization",
        "user__first_name"
    )

    specializations = (
        hospital.doctors
        .values_list(
            "specialization",
            flat=True
        )
        .distinct()
        .order_by("specialization")
    )

    return render(
        request,
        "hospitals/hospital_detail.html",
        {
            "hospital": hospital,
            "doctors": doctors,
            "specializations": specializations,
            "selected_specialization": specialization,
        }
    )