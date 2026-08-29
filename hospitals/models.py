from django.db import models


class Hospital(models.Model):

    HOSPITAL_TYPE_CHOICES = [
        ("Government", "Government"),
        ("Private", "Private"),
        ("Semi-Government", "Semi-Government"),
    ]

    name = models.CharField(
        max_length=200
    )

    registration_number = models.CharField(
        max_length=100,
        unique=True
    )

    hospital_type = models.CharField(
        max_length=30,
        choices=HOSPITAL_TYPE_CHOICES,
        default="Government"
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    pincode = models.CharField(
        max_length=10
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    emergency_available = models.BooleanField(
        default=False
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name