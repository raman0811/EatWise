import uuid

from django.db import models


class Meal(models.Model):

    class MealType(models.TextChoices):
        BREAKFAST = "BREAKFAST", "Breakfast"
        MORNING_SNACK = "MORNING_SNACK", "Morning Snack"
        LUNCH = "LUNCH", "Lunch"
        EVENING_SNACK = "EVENING_SNACK", "Evening Snack"
        DINNER = "DINNER", "Dinner"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    meal_type = models.CharField(
        max_length=20,
        choices=MealType.choices,
    )

    instructions = models.TextField(blank=True)

    prep_time = models.PositiveIntegerField(
        help_text="Preparation time in minutes."
    )

    cook_time = models.PositiveIntegerField(
        help_text="Cooking time in minutes."
    )

    servings = models.PositiveIntegerField(default=1)

    image_url = models.URLField(blank=True)

    # Nutrition values are stored per serving.
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
        default=0,
    )

    sodium = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class MealIngredient(models.Model):

    class QuantityUnit(models.TextChoices):
        GRAM = "G", "Gram"
        MILLILITER = "ML", "Milliliter"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
        related_name="meal_ingredients",
    )

    ingredient = models.ForeignKey(
        "nutrition.Ingredient",
        on_delete=models.PROTECT,
        related_name="meal_ingredients",
    )

    quantity = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    unit = models.CharField(
        max_length=5,
        choices=QuantityUnit.choices,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.meal.name} - {self.ingredient.name}"
    
class Tag(models.Model):

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
        max_length=100,
        unique=True,
    )

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MealTag(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
        related_name="meal_tags",
    )

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="meal_tags",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["meal", "tag"],
                name="unique_meal_tag",
            )
        ]

    def __str__(self):
        return f"{self.meal.name} - {self.tag.name}"

class MealDietaryPreference(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
        related_name="dietary_preferences",
    )

    dietary_preference = models.ForeignKey(
        "nutrition.DietaryPreference",
        on_delete=models.PROTECT,
        related_name="meals",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["meal", "dietary_preference"],
                name="unique_meal_dietary_preference",
            )
        ]

    def __str__(self):
        return f"{self.meal.name} - {self.dietary_preference.name}"