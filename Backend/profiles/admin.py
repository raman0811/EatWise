from django.contrib import admin

from .models import HealthProfile


@admin.register(HealthProfile)
class HealthProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_of_birth",
        "gender",
        "height",
        "current_weight",
        "activity_level",
        "goal",
        "created_at",
    )

    list_filter = (
        "gender",
        "activity_level",
        "goal",
    )

    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )