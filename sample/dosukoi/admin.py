from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Oyoyo

@admin.register(Oyoyo)
class OyoyoAdmin(admin.ModelAdmin):
    pass

