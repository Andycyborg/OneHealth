from django import forms
from django.utils import timezone

from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment

        fields = [
            "appointment_date",
            "appointment_time",
            "reason",
        ]

        widgets = {

            "appointment_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "appointment_time": forms.TimeInput(
                attrs={
                    "type": "time"
                }
            ),

            "reason": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": (
                        "Briefly describe the reason "
                        "for your visit..."
                    )
                }
            ),
        }

    def clean_appointment_date(self):

        date = self.cleaned_data.get(
            "appointment_date"
        )

        if date and date < timezone.localdate():

            raise forms.ValidationError(
                "Appointment date cannot be in the past."
            )

        return date