from django.db import models
from django.contrib.auth.models import User
import uuid


class CitizenProfile(models.Model):
    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("Unknown", "Unknown"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="citizen_profile"
    )

    onehealth_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True
    )

    blood_group = models.CharField(
        max_length=10,
        choices=BLOOD_GROUP_CHOICES,
        default="Unknown"
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    emergency_contact = models.CharField(
        max_length=15,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if not self.onehealth_id:
            self.onehealth_id = self.generate_onehealth_id()

        super().save(*args, **kwargs)

    @staticmethod
    def generate_onehealth_id():
        return "OH-" + uuid.uuid4().hex[:8].upper()

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.onehealth_id}"


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )

    doctor_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    specialization = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=200,
        blank=True
    )

    experience = models.PositiveIntegerField(
        default=0
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )
    hospitals = models.ManyToManyField(
    "hospitals.Hospital",
    related_name="doctors",
    blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if not self.doctor_id:
            self.doctor_id = "DOC-" + uuid.uuid4().hex[:8].upper()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"


class GovernmentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="government_profile"
    )

    officer_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    department = models.CharField(
        max_length=150
    )

    area = models.CharField(
        max_length=150,
        blank=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if not self.officer_id:
            self.officer_id = "GOV-" + uuid.uuid4().hex[:8].upper()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.department}"