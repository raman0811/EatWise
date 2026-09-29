from django.conf import settings
from django.db import models


class HealthProfile(models.Model):

    class HeightUnit(models.TextChoices):
        CM = "CM", "Centimeters"
        FT = "FT", "Feet"

    class WeightUnit(models.TextChoices):
        KG = "KG", "Kilograms"
        LB = "LB", "Pounds"

    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        OTHER = "OTHER", "Other"
        PREFER_NOT_TO_SAY = "PREFER_NOT_TO_SAY", "Prefer not to say"

    class ActivityLevel(models.TextChoices):
        SEDENTARY = "SEDENTARY", "Sedentary"
        LIGHTLY_ACTIVE = "LIGHTLY_ACTIVE", "Lightly Active"
        MODERATELY_ACTIVE = "MODERATELY_ACTIVE", "Moderately Active"
        VERY_ACTIVE = "VERY_ACTIVE", "Very Active"

    class Goal(models.TextChoices):
        WEIGHT_LOSS = "WEIGHT_LOSS", "Weight Loss"
        MAINTENANCE = "MAINTENANCE", "Weight Maintenance"
        WEIGHT_GAIN = "WEIGHT_GAIN", "Weight Gain"
        MUSCLE_BUILDING = "MUSCLE_BUILDING", "Muscle Building"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="health_profile",
    )

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=20,
        choices=Gender.choices,
    )

    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    height_unit = models.CharField(
        max_length=5,
        choices=HeightUnit.choices,
        default=HeightUnit.CM,
    )

    current_weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    weight_unit = models.CharField(
        max_length=5,
        choices=WeightUnit.choices,
        default=WeightUnit.KG,
    )

    activity_level = models.CharField(
        max_length=30,
        choices=ActivityLevel.choices,
    )

    goal = models.CharField(
        max_length=30,
        choices=Goal.choices,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}'s Health Profile"