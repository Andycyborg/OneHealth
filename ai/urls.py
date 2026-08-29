from django.urls import path

from . import views


app_name = "ai"


urlpatterns = [

    path(
        "summary/",
        views.citizen_summary,
        name="citizen_summary"
    ),

    path(
        "government/",
        views.government_summary,
        name="government_summary"
    ),

    path(
        "chatbot/",
        views.chatbot,
        name="chatbot"
    ),

]