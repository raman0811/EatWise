from django.contrib import admin

from .models import (
    HealthCondition,
    UserHealthCondition,
    Allergy,
    UserAllergy,
    DietaryPreference,
    UserDietaryPreference,
    Ingredient,
    Allergen,
    IngredientAllergen,
)


@admin.register(HealthCondition)
class HealthConditionAdmin(admin.ModelAdmin):
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


@admin.register(UserHealthCondition)
class UserHealthConditionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "condition",
        "created_at",
    )

    search_fields = (
        "user__email",
        "condition__name",
    )


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
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


@admin.register(UserAllergy)
class UserAllergyAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "allergy",
        "created_at",
    )

    search_fields = (
        "user__email",
        "allergy__name",
    )


@admin.register(DietaryPreference)
class DietaryPreferenceAdmin(admin.ModelAdmin):
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


@admin.register(UserDietaryPreference)
class UserDietaryPreferenceAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "preference",
        "created_at",
    )

    search_fields = (
        "user__email",
        "preference__name",
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "nutrition_basis_amount",
        "nutrition_basis_unit",
        "calories",
        "protein",
        "carbohydrates",
        "fat",
        "is_active",
    )

    list_filter = (
        "nutrition_basis_unit",
        "is_active",
    )

    search_fields = (
        "name",
    )


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
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


@admin.register(IngredientAllergen)
class IngredientAllergenAdmin(admin.ModelAdmin):
    list_display = (
        "ingredient",
        "allergen",
    )

    search_fields = (
        "ingredient__name",
        "allergen__name",
    )