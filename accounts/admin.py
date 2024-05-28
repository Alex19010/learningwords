from django.contrib import admin
from .models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("username", "email")
    list_display_links = list_display
    list_filter = ("username",)
    search_fields = ("username", "email")
