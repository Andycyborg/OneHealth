from django.urls import path

from . import views


app_name = "appointments"


urlpatterns = [

    path(
        "",
        views.appointment_list,
        name="list"
    ),

    path(
        "book/<int:hospital_id>/<int:doctor_id>/",
        views.book_appointment,
        name="book"
    ),

    path(
        "citizen/",
        views.citizen_appointments,
        name="citizen_appointments"
    ),

    path(
        "doctor/",
        views.doctor_appointments,
        name="doctor_appointments"
    ),

    path(
        "update/<int:appointment_id>/",
        views.update_appointment,
        name="update"
    ),

    path(
        "cancel/<int:appointment_id>/",
        views.cancel_appointment,
        name="cancel"
    ),
]