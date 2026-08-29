from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import (
    CitizenProfile,
    DoctorProfile,
    GovernmentProfile
)


class CitizenRegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )

    gender = forms.ChoiceField(
        choices=[
            ("", "Select Gender"),
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other"),
        ],
        required=False
    )

    blood_group = forms.ChoiceField(
        choices=CitizenProfile.BLOOD_GROUP_CHOICES,
        required=False
    )

    phone = forms.CharField(
        max_length=15,
        required=False
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False
    )

    emergency_contact = forms.CharField(
        max_length=15,
        required=False
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "date_of_birth",
            "gender",
            "blood_group",
            "phone",
            "address",
            "emergency_contact",
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:

            user.save()

            CitizenProfile.objects.create(
                user=user,
                date_of_birth=self.cleaned_data.get(
                    "date_of_birth"
                ),
                gender=self.cleaned_data.get(
                    "gender"
                ),
                blood_group=self.cleaned_data.get(
                    "blood_group"
                ) or "Unknown",
                phone=self.cleaned_data.get(
                    "phone"
                ),
                address=self.cleaned_data.get(
                    "address"
                ),
                emergency_contact=self.cleaned_data.get(
                    "emergency_contact"
                ),
            )

        return user


class DoctorRegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    specialization = forms.CharField(
        max_length=100
    )

    qualification = forms.CharField(
        max_length=200,
        required=False
    )

    experience = forms.IntegerField(
        min_value=0,
        required=False
    )

    phone = forms.CharField(
        max_length=15,
        required=False
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "specialization",
            "qualification",
            "experience",
            "phone",
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:

            user.save()

            DoctorProfile.objects.create(
                user=user,
                specialization=self.cleaned_data[
                    "specialization"
                ],
                qualification=self.cleaned_data[
                    "qualification"
                ],
                experience=self.cleaned_data.get(
                    "experience"
                ) or 0,
                phone=self.cleaned_data.get(
                    "phone"
                ),
            )

        return user


class GovernmentRegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    department = forms.CharField(
        max_length=150
    )

    area = forms.CharField(
        max_length=150,
        required=False
    )

    phone = forms.CharField(
        max_length=15,
        required=False
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "department",
            "area",
            "phone",
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:

            user.save()

            GovernmentProfile.objects.create(
                user=user,
                department=self.cleaned_data[
                    "department"
                ],
                area=self.cleaned_data[
                    "area"
                ],
                phone=self.cleaned_data[
                    "phone"
                ],
            )

        return user