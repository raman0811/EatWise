from django.core.management.base import BaseCommand
from nutrition.models import (
    HealthCondition,
    Allergy,
    DietaryPreference,
    Allergen,
    Ingredient,
    IngredientAllergen,
)


class Command(BaseCommand):
    help = "Seed initial EatWise nutrition reference data."

    def handle(self, *args, **options):

        # ============================================================
        # HEALTH CONDITIONS
        # ============================================================

        health_conditions = [
            {
                "name": "Diabetes",
                "code": "DIABETES",
                "description": "Dietary considerations related to diabetes.",
            },
            {
                "name": "High Blood Pressure",
                "code": "HIGH_BLOOD_PRESSURE",
                "description": "Dietary considerations related to high blood pressure.",
            },
            {
                "name": "High Cholesterol",
                "code": "HIGH_CHOLESTEROL",
                "description": "Dietary considerations related to high cholesterol.",
            },
            {
                "name": "PCOS",
                "code": "PCOS",
                "description": "Dietary considerations related to PCOS.",
            },
        ]

        for data in health_conditions:
            HealthCondition.objects.update_or_create(
                code=data["code"],
                defaults=data,
            )

        # ============================================================
        # ALLERGIES
        # ============================================================

        allergies = [
            {
                "name": "Peanuts",
                "code": "PEANUTS",
                "description": "Peanut allergy.",
            },
            {
                "name": "Tree Nuts",
                "code": "TREE_NUTS",
                "description": "Tree nut allergy.",
            },
            {
                "name": "Milk",
                "code": "MILK",
                "description": "Milk and dairy allergy.",
            },
            {
                "name": "Eggs",
                "code": "EGGS",
                "description": "Egg allergy.",
            },
            {
                "name": "Soy",
                "code": "SOY",
                "description": "Soy allergy.",
            },
            {
                "name": "Wheat",
                "code": "WHEAT",
                "description": "Wheat allergy.",
            },
            {
                "name": "Fish",
                "code": "FISH",
                "description": "Fish allergy.",
            },
            {
                "name": "Shellfish",
                "code": "SHELLFISH",
                "description": "Shellfish allergy.",
            },
        ]

        for data in allergies:
            Allergy.objects.update_or_create(
                code=data["code"],
                defaults=data,
            )

        # ============================================================
        # DIETARY PREFERENCES
        # ============================================================

        dietary_preferences = [
            {
                "name": "Vegetarian",
                "code": "VEGETARIAN",
                "description": "Does not include meat or fish.",
            },
            {
                "name": "Vegan",
                "code": "VEGAN",
                "description": "Excludes animal-derived foods.",
            },
            {
                "name": "Non-Vegetarian",
                "code": "NON_VEGETARIAN",
                "description": "Includes meat, poultry, fish, or other animal foods.",
            },
            {
                "name": "Eggetarian",
                "code": "EGGETARIAN",
                "description": "Vegetarian diet that includes eggs.",
            },
            {
                "name": "Pescatarian",
                "code": "PESCATARIAN",
                "description": "Vegetarian-style diet that includes fish.",
            },
        ]

        for data in dietary_preferences:
            DietaryPreference.objects.update_or_create(
                code=data["code"],
                defaults=data,
            )

        # ============================================================
        # ALLERGENS
        # ============================================================

        allergens = [
            {
                "name": "Peanuts",
                "code": "PEANUTS",
                "description": "Peanut allergen.",
            },
            {
                "name": "Tree Nuts",
                "code": "TREE_NUTS",
                "description": "Tree nut allergen.",
            },
            {
                "name": "Milk",
                "code": "MILK",
                "description": "Milk allergen.",
            },
            {
                "name": "Eggs",
                "code": "EGGS",
                "description": "Egg allergen.",
            },
            {
                "name": "Soy",
                "code": "SOY",
                "description": "Soy allergen.",
            },
            {
                "name": "Wheat",
                "code": "WHEAT",
                "description": "Wheat allergen.",
            },
            {
                "name": "Fish",
                "code": "FISH",
                "description": "Fish allergen.",
            },
            {
                "name": "Shellfish",
                "code": "SHELLFISH",
                "description": "Shellfish allergen.",
            },
        ]

        for data in allergens:
            Allergen.objects.update_or_create(
                code=data["code"],
                defaults=data,
            )

        # ============================================================
        # INGREDIENTS
        #
        # Nutrition values are per 100 g edible portion.
        #
        # Source:
        # ICMR-NIN Indian Food Composition Tables (IFCT) 2017
        #
        # Note:
        # sugar and sodium are nullable in the Ingredient model,
        # so None is used only where a reliable value is not loaded.
        # ============================================================

        ingredients = [
            {
                "name": "Rice, raw, milled",
                "description": "Raw milled rice.",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 356.36,
                "protein": 7.94,
                "carbohydrates": 78.24,
                "fat": 0.52,
                "fiber": 2.81,
                "sugar": None,
                "sodium": 2.34,
                "source": "ICMR-NIN IFCT 2017",
            },
            {
                "name": "Rice, raw, brown",
                "description": "Raw brown rice.",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 353.73,
                "protein": 9.16,
                "carbohydrates": 74.80,
                "fat": 1.24,
                "fiber": 4.43,
                "sugar": None,
                "sodium": 3.64,
                "source": "ICMR-NIN IFCT 2017",
            },
            {
                "name": "Ragi",
                "description": "Finger millet.",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 320.75,
                "protein": 7.16,
                "carbohydrates": 66.82,
                "fat": 1.92,
                "fiber": 11.18,
                "sugar": None,
                "sodium": 4.75,
                "source": "ICMR-NIN IFCT 2017",
            },
            {
                "name": "Wheat flour, atta",
                "description": "Whole wheat flour commonly used for Indian flatbreads.",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 320.27,
                "protein": 10.57,
                "carbohydrates": 64.17,
                "fat": 1.53,
                "fiber": 11.36,
                "sugar": None,
                "sodium": 2.04,
                "source": "ICMR-NIN IFCT 2017",
            },
            {
                "name": "Bengal gram, dal",
                "description": "Split Bengal gram (chickpea dal).",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 329.11,
                "protein": 21.55,
                "carbohydrates": 46.72,
                "fat": 5.31,
                "fiber": 15.15,
                "sugar": None,
                "sodium": 20.83,
                "source": "ICMR-NIN IFCT 2017",
            },
            {
                "name": "Bengal gram, whole",
                "description": "Whole Bengal gram (chickpea).",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 287.05,
                "protein": 18.77,
                "carbohydrates": 39.56,
                "fat": 5.11,
                "fiber": 25.22,
                "sugar": None,
                "sodium": 26.56,
                "source": "ICMR-NIN IFCT 2017",
            },
            {
                "name": "Green gram, dal",
                "description": "Split green gram (moong dal).",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 325.76,
                "protein": 23.88,
                "carbohydrates": 52.59,
                "fat": 1.35,
                "fiber": 9.37,
                "sugar": None,
                "sodium": 10.14,
                "source": "ICMR-NIN IFCT 2017",
            },
            {
                "name": "Lentil dal",
                "description": "Lentils used for dal preparations.",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 322.42,
                "protein": 24.35,
                "carbohydrates": 52.53,
                "fat": 0.75,
                "fiber": 10.43,
                "sugar": None,
                "sodium": 10.27,
                "source": "ICMR-NIN IFCT 2017",
            },
            {
                "name": "Rajmah, brown",
                "description": "Brown kidney beans.",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 297.56,
                "protein": 19.50,
                "carbohydrates": 48.83,
                "fat": 1.68,
                "fiber": 16.95,
                "sugar": None,
                "sodium": 10.47,
                "source": "ICMR-NIN IFCT 2017",
            },
            {
                "name": "Red gram dal",
                "description": "Split red gram (toor dal).",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 330.78,
                "protein": 21.70,
                "carbohydrates": 55.23,
                "fat": 1.56,
                "fiber": 9.06,
                "sugar": None,
                "sodium": 18.01,
                "source": "ICMR-NIN IFCT 2017",
            },

            # --------------------------------------------------------
            # EGG
            # IFCT M001
            # Carbohydrate and dietary fibre are reported as 0.
            # --------------------------------------------------------

            {
                "name": "Egg, poultry, whole, raw",
                "description": "Whole raw poultry egg.",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 134.83,
                "protein": 13.28,
                "carbohydrates": 0,
                "fat": 9.15,
                "fiber": 0,
                "sugar": None,
                "sodium": 123.00,
                "source": "ICMR-NIN IFCT 2017",
            },

            # --------------------------------------------------------
            # CHICKEN
            # IFCT N003
            # Carbohydrate and dietary fibre are reported as 0.
            # --------------------------------------------------------

            {
                "name": "Chicken, breast, skinless",
                "description": "Raw skinless chicken breast.",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 168.26,
                "protein": 21.81,
                "carbohydrates": 0,
                "fat": 9.00,
                "fiber": 0,
                "sugar": None,
                "sodium": None,
                "source": "ICMR-NIN IFCT 2017",
            },

            # --------------------------------------------------------
            # MILK
            # IFCT L002
            # --------------------------------------------------------

            {
                "name": "Milk, whole, cow",
                "description": "Whole cow's milk.",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 72.90,
                "protein": 3.26,
                "carbohydrates": 4.94,
                "fat": 4.48,
                "fiber": 0,
                "sugar": None,
                "sodium": 25.46,
                "source": "ICMR-NIN IFCT 2017",
            },

            # --------------------------------------------------------
            # PANEER
            # IFCT L003
            # --------------------------------------------------------

            {
                "name": "Paneer",
                "description": "Indian fresh cheese (paneer).",
                "nutrition_basis_amount": 100,
                "nutrition_basis_unit": "G",
                "calories": 305.45,
                "protein": 18.86,
                "carbohydrates": 2.41,
                "fat": 24.78,
                "fiber": 0,
                "sugar": None,
                "sodium": 18.04,
                "source": "ICMR-NIN IFCT 2017",
            },
        ]

        for data in ingredients:
            Ingredient.objects.update_or_create(
                name=data["name"],
                defaults=data,
            )

        # ============================================================
        # INGREDIENT -> ALLERGEN RELATIONSHIPS
        # ============================================================

        allergen_relationships = [
            ("Wheat flour, atta", "WHEAT"),
            ("Egg, poultry, whole, raw", "EGGS"),
            ("Milk, whole, cow", "MILK"),
            ("Paneer", "MILK"),
        ]

        for ingredient_name, allergen_code in allergen_relationships:

            ingredient = Ingredient.objects.get(
                name=ingredient_name,
            )

            allergen = Allergen.objects.get(
                code=allergen_code,
            )

            IngredientAllergen.objects.update_or_create(
                ingredient=ingredient,
                allergen=allergen,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "EatWise seed data loaded successfully."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Health conditions: {HealthCondition.objects.count()}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Allergies: {Allergy.objects.count()}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Dietary preferences: {DietaryPreference.objects.count()}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Allergens: {Allergen.objects.count()}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Ingredients: {Ingredient.objects.count()}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Ingredient-allergen relationships: "
                f"{IngredientAllergen.objects.count()}"
            )
        )