from django.urls import path

from . import views


app_name = "records"


urlpatterns = [

    path(
        "patient/<int:patient_id>/",
        views.doctor_patient_records,
        name="doctor_patient_records"
    ),

    path(
        "search-patient/",
        views.search_patient_records,
        name="search_patient_records"
    ),

    path(
        "create/<int:patient_id>/",
        views.create_medical_record,
        name="create_medical_record"
    ),

    path(
        "create/<int:patient_id>/<int:appointment_id>/",
        views.create_medical_record,
        name="create_medical_record_appointment"
    ),

    path(
        "my/",
        views.citizen_records,
        name="citizen_records"
    ),

    path(
        "prescription/<int:record_id>/",
        views.add_prescription,
        name="add_prescription"
    ),

]