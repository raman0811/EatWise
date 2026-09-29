import uuid

from django.db import models


class HealthCondition(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class UserHealthCondition(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="health_conditions",
    )

    condition = models.ForeignKey(
        HealthCondition,
        on_delete=models.CASCADE,
        related_name="users",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "condition"],
                name="unique_user_health_condition",
            )
        ]

    def __str__(self):
        return f"{self.user.email} - {self.condition.name}"


class Allergy(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class UserAllergy(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="allergies",
    )

    allergy = models.ForeignKey(
        Allergy,
        on_delete=models.CASCADE,
        related_name="users",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "allergy"],
                name="unique_user_allergy",
            )
        ]

    def __str__(self):
        return f"{self.user.email} - {self.allergy.name}"


class DietaryPreference(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class UserDietaryPreference(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="dietary_preferences",
    )

    preference = models.ForeignKey(
        DietaryPreference,
        on_delete=models.CASCADE,
        related_name="users",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "preference"],
                name="unique_user_dietary_preference",
            )
        ]

    def __str__(self):
        return f"{self.user.email} - {self.preference.name}"


class Ingredient(models.Model):

    class NutritionBasisUnit(models.TextChoices):
        GRAM = "G", "Gram"
        MILLILITER = "ML", "Milliliter"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    nutrition_basis_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=100,
    )

    nutrition_basis_unit = models.CharField(
        max_length=5,
        choices=NutritionBasisUnit.choices,
        default=NutritionBasisUnit.GRAM,
    )

    calories = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    protein = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    carbohydrates = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    fat = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    fiber = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    sugar = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
)

    sodium = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
)

    source = models.CharField(
        max_length=100,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Allergen(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class IngredientAllergen(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="allergens",
    )

    allergen = models.ForeignKey(
        Allergen,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["ingredient", "allergen"],
                name="unique_ingredient_allergen",
            )
        ]

    def __str__(self):
        return f"{self.ingredient.name} - {self.allergen.name}"