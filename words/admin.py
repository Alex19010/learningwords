from django.contrib import admin
from .models import Section, Word


@admin.register(Section)
class AdminSection(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = list_display
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Word)
class AdminWord(admin.ModelAdmin):
    list_display = ('foreign_word', 'native_word', 'section')
    list_display_links = list_display
    list_filter = ('foreign_word', 'native_word', 'section')
    search_fields = ('foreign_word', 'native_word', 'section')
