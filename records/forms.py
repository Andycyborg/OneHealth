from django import forms

from .models import MedicalRecord, Prescription


class MedicalRecordForm(forms.ModelForm):

    class Meta:

        model = MedicalRecord

        fields = [
            "diagnosis",
            "symptoms",
            "notes",
        ]

        widgets = {

            "diagnosis": forms.TextInput(
                attrs={
                    "placeholder":
                    "Example: Viral Fever"
                }
            ),

            "symptoms": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),
        }


class PrescriptionForm(forms.ModelForm):

    class Meta:

        model = Prescription

        fields = [
            "medicine_name",
            "dosage",
            "frequency",
            "duration",
            "instructions",
        ]

        widgets = {

            "instructions": forms.Textarea(
                attrs={
                    "rows": 3
                }
            ),
        }