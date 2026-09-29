from django.contrib import admin

from .models import (
    Meal,
    MealIngredient,
    MealTag,
    Tag,
    MealDietaryPreference,
)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "meal_type",
        "calories",
        "protein",
        "is_active",
        "created_at",
    )

    list_filter = (
        "meal_type",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )


@admin.register(MealIngredient)
class MealIngredientAdmin(admin.ModelAdmin):
    list_display = (
        "meal",
        "ingredient",
        "quantity",
        "unit",
    )

    list_filter = (
        "unit",
    )

    search_fields = (
        "meal__name",
        "ingredient__name",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )


@admin.register(MealTag)
class MealTagAdmin(admin.ModelAdmin):
    list_display = (
        "meal",
        "tag",
    )

    search_fields = (
        "meal__name",
        "tag__name",
    )


@admin.register(MealDietaryPreference)
class MealDietaryPreferenceAdmin(admin.ModelAdmin):
    list_display = (
        "meal",
        "dietary_preference",
    )

    search_fields = (
        "meal__name",
        "dietary_preference__name",
    )