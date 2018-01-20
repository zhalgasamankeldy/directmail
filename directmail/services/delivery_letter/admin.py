from django.contrib import admin

# Register your models here.
from .models import DeliveryType, Letter

@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    search_fields = ["name"]


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "delivery_type", "customer", "date_created"]
